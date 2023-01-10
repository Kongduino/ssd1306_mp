# ssd1306_mp

A fork of the [ssd1206 library for Micropython](https://github.com/stlehmann/micropython-ssd1306/) I have found, quite well written. This fork adds the `rotate180()` method, which was absent. I am planning to add more features as I go. I pushed a [PR](https://github.com/stlehmann/micropython-ssd1306/pull/7).

Tested on an [Elecfreaks Wukong 2040](https://shop.elecfreaks.com/products/elecfreaks-wukong2040-expansion-board-adapter-for-raspberry-pi-pico), donated by [Elecfreaks](https://github.com/elecfreaks), and an original Pico.

## Commands I added:

* `rotate`: Set this variable to `True` or `False` to rotate the display automatically. The library's `show()` function calls `rotate180()` when needed.
* `rotate180()`: self-explanatory I believe...
* `drawOval(self, cX, cY, rX, rY)`: draws an oval centered on cX, cY. Radius X and Y determine the shape.
* `drawCircle(self, cX, cY, radius)`: calls `drawCircle` with 2 identical radii.
* `fillOval(self, cX, cY, radius)`: draws a filled disk centered on cX, cY, in white (1, default) or black (0). Radius X and Y determine the shape.
* `fillCircle(self, cX, cY, radius)`: calls `fillCircle` with 2 identical radii.

## Timer

I am using at the end of the current demo a `Timer` object to display an animation that runs on its own. I updated the demo GIF, see for yourself. The animation keeps running, although the program ended.


![demo](demo.gif)