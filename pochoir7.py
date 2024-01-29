#!/Applications/GIMP.app/Contents/MacOS/python

from gimpfu import *
import gimp

def pochoir7(image, layer):
    modethreshold = 5 # histogram luminance
    contrast = 0.3
    brightness = 0.25
    lowthreshold=0.0
    highthreshold=1.0
    pdb.gimp_image_undo_group_start(image)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_drawable_brightness_contrast(drawable, brightness, contrast)
    # create layers
    layer0 = layer.copy()
    layer1 = layer.copy()
    layer2 = layer.copy()
    layer3 = layer.copy()
    layer4 = layer.copy()
    layer5 = layer.copy()
    layer6 = layer.copy()
    layer0.name="0%"
    layer1.name="17%"
    layer2.name="33%"
    layer3.name="100%"
    layer4.name="83%"
    layer5.name="66%"
    layer6.name="50%"
    image.add_layer(layer6, 0)
    image.add_layer(layer5, 0)
    image.add_layer(layer4, 0)
    image.add_layer(layer3, 0)
    image.add_layer(layer2, 0)
    image.add_layer(layer1, 0)
    image.add_layer(layer0, 0)

    #layer0
    lowthreshold=0.08333
    pdb.gimp_image_set_active_layer(image, layer0)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_drawable_threshold(drawable,modethreshold,lowthreshold,highthreshold)
    pdb.gimp_drawable_invert(drawable, TRUE)
    mask = pdb.gimp_layer_create_mask(layer0,5) # 5 for mask copy
    pdb.gimp_layer_add_mask(layer0, mask)
    pdb.gimp_context_set_foreground((0,0,0))
    pdb.gimp_drawable_fill(drawable, 0)

    #layer1
    lowthreshold=0.25
    pdb.gimp_image_set_active_layer(image, layer1)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_drawable_threshold(drawable,modethreshold,lowthreshold,highthreshold)
    pdb.gimp_drawable_invert(drawable, TRUE)
    mask = pdb.gimp_layer_create_mask(layer1,5) # 5 for mask copy
    pdb.gimp_layer_add_mask(layer1, mask)
    pdb.gimp_context_set_foreground((43,43,43))
    pdb.gimp_drawable_fill(drawable, 0)

    #layer2
    lowthreshold=0.416666
    pdb.gimp_image_set_active_layer(image, layer2)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_drawable_threshold(drawable,modethreshold,lowthreshold,highthreshold)
    pdb.gimp_drawable_invert(drawable, TRUE)
    mask = pdb.gimp_layer_create_mask(layer2,5) # 5 for mask copy
    pdb.gimp_layer_add_mask(layer2, mask)
    pdb.gimp_context_set_foreground((85,85,85))
    pdb.gimp_drawable_fill(drawable, 0)

    #layer3
    lowthreshold=0.916666
    pdb.gimp_image_set_active_layer(image, layer3)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_drawable_threshold(drawable,modethreshold,lowthreshold,highthreshold)
    mask = pdb.gimp_layer_create_mask(layer3,5) # 5 for mask copy
    pdb.gimp_layer_add_mask(layer3, mask)
    pdb.gimp_context_set_foreground((255,255,255)) 
    pdb.gimp_drawable_fill(drawable, 0)

    #layer4
    lowthreshold=0.75
    pdb.gimp_image_set_active_layer(image, layer4)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_drawable_threshold(drawable,modethreshold,lowthreshold,highthreshold)
    mask = pdb.gimp_layer_create_mask(layer4,5) # 5 for mask copy
    pdb.gimp_layer_add_mask(layer4, mask)
    pdb.gimp_context_set_foreground((213,213,213))
    pdb.gimp_drawable_fill(drawable, 0)

    #layer5
    lowthreshold=0.583333
    pdb.gimp_image_set_active_layer(image, layer5)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_drawable_threshold(drawable,modethreshold,lowthreshold,highthreshold)
    mask = pdb.gimp_layer_create_mask(layer5,5) # 5 for mask copy
    pdb.gimp_layer_add_mask(layer5, mask)
    pdb.gimp_context_set_foreground((171,171,171))
    pdb.gimp_drawable_fill(drawable, 0)

    #layer6
    lowthreshold=0.5
    pdb.gimp_image_set_active_layer(image, layer6)
    drawable = pdb.gimp_image_get_active_drawable(image)
    pdb.gimp_drawable_threshold(drawable,modethreshold,lowthreshold,highthreshold)
    mask = pdb.gimp_layer_create_mask(layer6,0) # 0 for white mask
    pdb.gimp_layer_add_mask(layer6, mask)
    pdb.gimp_context_set_foreground((128,128,128)) 
    pdb.gimp_drawable_fill(drawable, 0)

    pdb.gimp_image_undo_group_end(image)
    

register(
    "python-fu-pochoir7",
    "Create a multilayered stencil.",
    "Given an image, automatically create a set of stencil masks.",
    "David Carter", "David Carter", "2020",
    "<Image>/Filters/Pochoir7",
    "",
    [],
    [],
    pochoir7)

main()
