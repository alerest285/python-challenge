### Python Challenge for GSOC JDE Robot:

implementation of brownian motion in python.

 The position of the ball is given as a complex number `z = x + i*y`, being `x` and `y` the (real) coordinates.  
 Movement is done by adding a small step in a given direction:  
  
`z' = z + (s) * e^{i\theta}`
  
  `s`  is the magnitude of the step,  
  `theta` is the angle of the direction.
If the particle hasnt hit a wall, it continues in the same direction.  
 If it hits the wall a new random angle is chosen to simulate bouncing, the magnitude of the change can be altered using the multiplier.  

---







