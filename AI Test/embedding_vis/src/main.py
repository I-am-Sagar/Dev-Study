from utils.image_utils import load_image, preprocess_image
from models.clip import CLIPModel

def main():
    clip_model = CLIPModel()

    print("Loading Image...")
    image = load_image('sample.jpg')

    print("Preprocessing Image...")
    preprocessed_image = preprocess_image(image=image, clip_model=clip_model)

    print("Computing embedding...")
    image_embedding = clip_model.get_image_embedding(preprocessed_image=preprocessed_image)

    print(f"Image embedding shape: {image_embedding.shape}")
    print(f"First few values of embedding: {image_embedding[0, :5]}")


if __name__ == "__main__":
    main()