import iri
import sample

for key, value in sample.files_properties.items():
    print("{}: {}".format(key, sample.font.paint(value[1], sample.font.beige)))
