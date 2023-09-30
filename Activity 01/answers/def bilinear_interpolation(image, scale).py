def bilinear_interpolation(image, scale):
    height, width, channels = image.shape
    h_zoom, w_zoom = height*scale, width*scale

    image_zoom = np.zeros((h_zoom, w_zoom, channels), dtype = np.float32)

    for h in range(h_zoom):
        for w in range(w_zoom):
            for c in range(channels):

                if ((h+1)%scale==0 and (w+1)%scale==0):
                    image_zoom[h][w][c] = image[int((h+1)/scale) - 1][int((w+1)/scale) - 1][c]
                
                elif ((h+1)%scale==0):
                    if (w<scale):
                        image_zoom[h][w][c] = (w+1)/scale * image[int((h+1)/scale) - 1][0][c]
                    else:
                        image_zoom[h][w][c] = (1 - (w+1)%scale/scale) * image[int((h+1)/scale) - 1][int((w+1)/scale) - 1][c] + (w+1)%scale/scale * image[int((h+1)/scale) - 1][int((w+1)/scale)][c]

                elif ((w+1)%scale==0):
                    if (h<scale):
                        image_zoom[h][w][c] = (h+1)/scale * image[0][int((w+1)/scale) - 1][c]
                    else:
                        image_zoom[h][w][c] = (1 - (h+1)%scale/scale) * image[int((h+1)/scale) - 1][int((w+1)/scale) - 1][c] + (h+1)%scale/scale * image[int((h+1)/scale)][int((w+1)/scale) - 1][c]

                else:
                    if (h<scale and w<scale):
                        image_zoom[h][w][c] = (w+1)%scale/scale * (h+1)%scale/scale * image[0][0][c]
                    elif (h<scale):
                        image_zoom[h][w][c] = (h+1)%scale/scale * ((1 - (w+1)%scale/scale) * image[int((h+1)/scale) - 1][int((w+1)/scale) - 1][c] + (w+1)%scale/scale * image[int((h+1)/scale) - 1][int((w+1)/scale)][c])
                    elif (w<scale):
                        image_zoom[h][w][c] = (w+1)%scale/scale * ((1 - (h+1)%scale/scale) * image[int((h+1)/scale) - 1][int((w+1)/scale) - 1][c] + (h+1)%scale/scale * image[int((h+1)/scale)][int((w+1)/scale) - 1][c])
                    else:
                        a = (1 - (h+1)%scale/scale) * image[int((h+1)/scale) - 1][int((w+1)/scale) - 1][c] + (h+1)%scale/scale * image[int((h+1)/scale)][int((w+1)/scale) - 1][c]
                        b = (1 - (h+1)%scale/scale) * image[int((h+1)/scale) - 1][int((w+1)/scale)][c] + (h+1)%scale/scale * image[int((h+1)/scale)][int((w+1)/scale)][c]
                        image_zoom[h][w][c] = (1 - (w+1)%scale/scale) * a + (w+1)%scale/scale * b

    return image_zoom.astype(np.uint8)