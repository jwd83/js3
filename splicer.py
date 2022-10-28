
import pygame
import sys
import os


def main():
    pygame.init()
    print("JS³ :: Jared's Sprite Sheet Splicer")

    # check for the filename and dimension being passed
    if len(sys.argv) != 3:
        print("Usage:   python splice.py <filename> <square pixel dimension>")
        print("Example: python splice.py player.png 16")
        sys.exit(1)

    # store the filename and dimension
    filename = sys.argv[1]
    filename_without_extension = os.path.splitext(filename)[0]
    dimension = int(sys.argv[2])

    # load the image file and get the width and height of it
    image = pygame.image.load(filename)
    width, height = image.get_size()

    if width < dimension or height < dimension:
        print("The image is smaller than the dimension")
        sys.exit(1)

    # calculate the number of rows and columns
    rows = height // dimension
    columns = width // dimension

    for row in range(rows):
        for column in range(columns):
            # create a new transparent surface for each row and column
            # and blit the image to it and save it
            surface = pygame.Surface((dimension, dimension), pygame.SRCALPHA)
            surface.blit(image, (0, 0), (column * dimension,
                         row * dimension, dimension, dimension))

            # save the surface to a file
            output_name = f"{filename_without_extension}_{row}_{column}.png"

            # check if the file already exists
            if os.path.exists(output_name):
                print(f"{output_name} already exists. Skipping this image")

            else:
                print("Saving", output_name)

                # save the image file to disk
                pygame.image.save(surface, output_name)


if __name__ == '__main__':
    main()
