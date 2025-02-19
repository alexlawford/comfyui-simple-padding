# Simple Padding

Simple padding takes as inputs the following:

**X1**, integer: the x coordinate of the top-left point of your box

**Y1**, integer: the y coordinate of the top-left point of your box

**X2**, integer: the x coordinate of the bottom-right point of your box

**Y2**, integer: the y coordinate of the bottom-right point of your box

**max_X**, integer: the maximum x cordinate that should be returned

**max_Y**, integer: the maximum y cordinate that should be returned

**padding**, the number to pad by

It returns:

**X1**, **Y1** the top-left coordinates of the padded box and **X2**, **Y2** the bottom-right coordinates of the padded box.