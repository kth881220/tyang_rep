import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import pygame
import sys

# ============================================================
# Step 1: Train a CNN model on the MNIST handwritten digit dataset
# ============================================================

def build_and_train_model():
    print("Loading MNIST dataset...")
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
    x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

    model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation="relu"),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(10, activation="softmax"),
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    print("Training model...")
    model.fit(x_train, y_train, epochs=3, batch_size=128, validation_split=0.1, verbose=1)

    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    print(f"Test accuracy: {accuracy:.4f}")

    return model


# ============================================================
# Step 2: Pygame drawing canvas for handwritten digit input
# ============================================================

def run_drawing_app(model):
    pygame.init()

    WIDTH, HEIGHT = 400, 450
    CANVAS_SIZE = 400
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    BLUE = (50, 100, 200)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Handwritten Digit Recognition")

    canvas = pygame.Surface((CANVAS_SIZE, CANVAS_SIZE))
    canvas.fill(BLACK)

    font = pygame.font.SysFont(None, 36)
    small_font = pygame.font.SysFont(None, 24)

    drawing = False
    prediction_text = "Draw a digit (0-9)"
    confidence_text = ""

    def predict_digit():
        nonlocal prediction_text, confidence_text

        pixel_data = pygame.surfarray.array3d(canvas)
        pixel_data = pixel_data[:, :, 0]  # grayscale (take one channel)
        pixel_data = pixel_data.T  # transpose to correct orientation

        img = Image.fromarray(pixel_data.astype("uint8"), mode="L")
        img = img.resize((28, 28), Image.LANCZOS)

        img_array = np.array(img).astype("float32") / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        pred = model.predict(img_array, verbose=0)
        digit = np.argmax(pred[0])
        conf = pred[0][digit] * 100

        prediction_text = f"Prediction: {digit}"
        confidence_text = f"Confidence: {conf:.1f}%"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] < CANVAS_SIZE:
                    drawing = True

            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                predict_digit()

            elif event.type == pygame.MOUSEMOTION and drawing:
                if event.pos[1] < CANVAS_SIZE:
                    pygame.draw.circle(canvas, WHITE, event.pos, 15)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    canvas.fill(BLACK)
                    prediction_text = "Draw a digit (0-9)"
                    confidence_text = ""
                elif event.key == pygame.K_q:
                    running = False

        screen.fill(GRAY)
        screen.blit(canvas, (0, 0))

        pred_surface = font.render(prediction_text, True, BLUE)
        screen.blit(pred_surface, (10, CANVAS_SIZE + 10))

        if confidence_text:
            conf_surface = small_font.render(confidence_text, True, BLACK)
            screen.blit(conf_surface, (10, CANVAS_SIZE + 40))

        help_surface = small_font.render("C: Clear | Q: Quit", True, BLACK)
        screen.blit(help_surface, (WIDTH - 170, CANVAS_SIZE + 10))

        pygame.display.flip()

    pygame.quit()


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    model = build_and_train_model()
    print("\n--- Drawing window is opening ---")
    print("Draw a digit with your mouse. Release to predict.")
    print("Press C to clear, Q to quit.\n")
    run_drawing_app(model)
