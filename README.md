# BDSP Map Matrix Editor

![image](https://user-images.githubusercontent.com/56665250/182005464-a3796ef5-e51b-4d5e-a76b-422e6dc33e0b.png)

## Loading Matrix

The author of this application makes the assumption that you have a general idea of what you're trying to do, and will not provide instructions on how to acquire the data that this application can modify.

However, assuming you do have that, select File > Load and select your "romfs" folder. The app will begin iterating over some data and may take a while depending on your computer. Recommend opening the tool from a command shell so you can see the loading progress. Once this loading is done for the first time, you will have a "romfs_unpacked" folder in the same directory of your "romfs" folder. On future runs of the application, when the romfs folder is selected, you will be asked if you want to use the already unpacked files. If you select no, they will be unpacked from scratch again.


## Editing Cells

Select any cell and its data will fill in the fields on the left. Make any necessary changes and save them by clicking the Save Cell button.
Save all changes to the matrix by clicking the Save Matrix button.

The width and height of the matrix can be edited by using the boxes near the bottom left. Unset matrix cells will appear red and will stay red until explicitly set otherwise.

## Events Tab

This tool supports viewing Collision and Ex attributes for selected cells. It will display this grid over map images that were exported from DP using this fork of [DSPRE](https://github.com/ycdevbdsp/DS-Pokemon-Rom-Editor) for help. 

This tab shows placedata entries for the loaded map area. Its attributes can be modified using the fields on the right. Selecting one will populate the fields with its current data, and clicking an empty cell will allow you to create a new placedata entry for the loaded map. Make your changes and click "Save Event" to save changes to the event. Click the "Save Map" button in the bottom left to save all your changes to file.

![image](https://user-images.githubusercontent.com/56665250/211706226-2023aa90-1b8c-4c60-a4e9-e6dac6cb6feb.png)

## Collision Tab

The only tiles that  matter here are the first two, 00 and 01. White is no collision and red is collision. You can select either and then draw collision on the map like you were drawing in Paint. Click the "Save Map" button to save your changes to the collision file.

![image](https://user-images.githubusercontent.com/56665250/211705773-0df22ffe-c733-48d2-8adc-72bb2d70da11.png)


## Ex Attributes Tab

This tab allows you to set attributes of each tile, e.g. the sound effect that plays when walking over dirt. Drawing tiles works the same way as the Collision tab. Click the "Save Map" button to save your changes to the attribute file.


## Outputs

All files saved are currently written to the "output" folder. This will be updated later to be saved into a structure that can be used with [Ai0796's repacker](https://github.com/Ai0796/BDSP-Repacker). But for the time being, it's assumed you know what to do with the respective output files.
