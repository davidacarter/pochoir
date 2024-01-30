# pochoir

A GIMP plugin to convert any normal image into a stacked set of stencil layers. Useful for planning physical multilayer stencil paintings based on digital artwork or photography.


# Getting started

## Installation
See https://en.wikibooks.org/wiki/GIMP/Installing_Plugins

## Usage
1. Load any image in GIMP and click on the Filters menu.
2. You should now see `Pochoir7` as one of the filter choices.
3. Click `Pochoir7` and you should see a set of layers automatically created to break the image into 7 grayscale layers.
4. These can be cut as physical stencils and used to create photorealistic multilayered stencil paintings.
5. To simplify to 3 layers, just delete all layers except for 100%, 50%, and 0%.

# Example

## Before
![Before](https://github.com/davidacarter/pochoir/blob/main/before.png)
## After
![After](https://github.com/davidacarter/pochoir/blob/main/after.png)

Note the separated layer masks at lower right. The main image is now comprised of a stack of greyscale masks with transparent regions allowing underlying tones to stack correctly as a multilayer stencil.
