# pochoir

A GIMP plugin to convert any normal image into a stacked set of stencil layers. Useful for planning physical multilayer stencil paintings based on digital artwork or photography.


# Getting started

## Installation
See https://en.wikibooks.org/wiki/GIMP/Installing_Plugins

## Usage
1. Load any image in GIMP and click on the Filters menu.
2. You should see `Pochoir7` as one of the filter choices.
3. Click `Pochoir7` and you should see a set of layers automatically created to break the image into 7 grayscale layers.
4. The layer named "0%" has the darkest tones and the one named "100%" has the brightest white tones. The others are evenly spaced shades of gray.
5. These masks can be used to cut a set of physical stencils to achieve photorealistic aerosol painting effects.
6. To simplify to 3 layers, just disregard all layers except for 100%, 50%, and 0%. This will reduce detail and increase contrast but can yield nice results with less effort.

# Example

## Before
![Before](https://github.com/davidacarter/pochoir/blob/main/before.png)
## After
![After](https://github.com/davidacarter/pochoir/blob/main/after.png)

Note the separated layer masks at lower right. The main image is now comprised of a stack of greyscale masks with transparent regions allowing underlying tones to stack correctly as a set of multilayer stencil guides. These can be sent to a printer or laser cutting device.
