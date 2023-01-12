# ssd1306_mp

A fork of the [ssd1206 library for Micropython](https://github.com/stlehmann/micropython-ssd1306/) I have found, quite well written. This fork originally added the `rotate180()` method, which was absent. And then I started adding more features. I pushed a [PR](https://github.com/stlehmann/micropython-ssd1306/pull/7), but the project seems dormant.

This is being tested on an [Elecfreaks Wukong 悟空 2040](https://shop.elecfreaks.com/products/elecfreaks-wukong2040-expansion-board-adapter-for-raspberry-pi-pico), donated by [Elecfreaks](https://github.com/elecfreaks), and an original Pico.

## Commands I added:

* `rotate`: Set this variable to `True` or `False` to rotate the display automatically. The library's `show()` function calls `rotate180()` when needed.
* `rotate180()`: self-explanatory I believe...
* `drawOval(self, cX, cY, rX, rY)`: draws an oval centered on cX, cY. Radius X and Y determine the shape.
* `drawCircle(self, cX, cY, radius)`: calls `drawCircle` with 2 identical radii.
* `fillOval(self, cX, cY, radius)`: draws a filled disk centered on cX, cY, in white (1, default) or black (0). Radius X and Y determine the shape.
* `fillCircle(self, cX, cY, radius)`: calls `fillCircle` with 2 identical radii.
* `drawLines(self, lines, clr = 1)`: draws lines from an array `lines[]` of points. Needs a multiple of 4 ints.
* `drawConnectedLines(self, lines, clr = 1)`: draws connected lines from an array `lines[]` of 4 points. Needs a multiple of 2 ints, minimum 4 in total. The end point of a line becomes the start point of the next line.

There is a `floodFill()` method, but it's not working well. I need to improve it.

## Timer

I am using at the end of the current demo a `Timer` object to display an animation that runs on its own. I updated the demo GIF, see for yourself. The animation keeps running, although the program ended.


![demo](demo.gif)