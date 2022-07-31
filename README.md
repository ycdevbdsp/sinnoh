# BDSP Map Matrix Editor

![image](https://user-images.githubusercontent.com/56665250/181406727-dfa8c5c4-692b-4b88-bd0d-b01416e13aa4.png)

## Loading Matrix

The author of this application makes the assumption that you have a general idea of what you're trying to do, and will not provide instructions on how to acquire the data that this application can modify.

However, assuming you do have that, select File > Load and select the file that contains the map matrix files (hint: it's called "gamesettings"). The app will begin iterating over some data and may take a while depending on your computer. Recommend opening the tool from a command shell so you can see the loading progress.


## Editing Cells

Select any cell and its data will fill in the fields on the left. Make any necessary changes and save them by clicking the Save Cell button.
Save all changes to the matrix by clicking the Save Matrix button.

The width and height of the matrix can be edited by using the boxes near the bottom left. Unset matrix cells will appear red and will stay red until explicitly set otherwise.

## Viewing Collision

This tool supports viewing Collision and Ex attributes for selected cells. It will display this grid over map images if the images are provided. This app doesn't provide it for you. Check out this fork of [DSPRE](https://github.com/ycdevbdsp/DS-Pokemon-Rom-Editor) for help.

![image](https://user-images.githubusercontent.com/56665250/182005422-452a2327-78dd-415b-9c58-da80b1ecc846.png)
