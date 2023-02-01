from matplotlib import pyplot as plt
import numpy as np
from os import listdir as ls
import sys
import importlib.util
import os

sys.dont_write_bytecode = True  # Impede de produzir __pycache__

# Definição de parâmetros universais

plt.rcParams["figure.figsize"] = (9, 5)
plt.style.use("ggplot")
ihm_navy = (.19, .29, .66)
dpi = 200
extension = "png"
image_dir = "figuras"

generator_dir = "code/image_generators"
generators = ls(generator_dir)

if __name__ == "__main__":

    for generator_file_name in generators:
        file_path = generator_dir+"/"+generator_file_name
        generator_name = generator_file_name[:-3]
        image_path = image_dir+"/"+generator_name

        if not os.path.exists(image_path+f".{extension}"):

            # Next few lines imports image generator function from each file

            spec = importlib.util.spec_from_file_location(generator_name,
                                                          file_path)

            generator_class = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(generator_class)
            generate = getattr(generator_class, generator_name)

            # Generates image
            generate(ihm_navy, dpi, image_path, extension)
