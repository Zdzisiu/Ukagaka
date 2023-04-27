from PIL import Image
from sys import argv

if argv[1].lower() == "color":
    size = [int(argv[2]),int(argv[3])]
    color = [int(argv[4]),int(argv[5]),int(argv[6]),int(argv[7])]
    image =  Image.new("RGBA", (size[0], size[1]), (color[0], color[1], color[2], color[3]))
    image.save(str(argv[8])+'.png')
elif argv[1].lower() == "resize_org_ratio":
    img = Image.open(argv[2])
    new_size = (int(argv[3]), int(argv[4]))
    original_ratio = img.size[0] / img.size[1]
    new_ratio = new_size[0] / new_size[1]
    if original_ratio > new_ratio:
        new_width = int(new_size[1] * original_ratio)
        new_height = new_size[1]
    else:
        new_width = new_size[0]
        new_height = int(new_size[0] / original_ratio)
    img = img.resize((new_width, new_height))
    img.save(argv[5])
elif argv[1].lower() == "resize_new_ratio":
    img = Image.open(argv[2])
    new_size = (int(argv[3]), int(argv[4]))
    img = img.resize((new_size[0], new_size[1]))
    img.save(argv[5])
elif argv[1].lower() == "overlayfast_merge":
    base_img = Image.open(argv[2]).convert("RGBA")
    overlay_img = Image.open(argv[3]).convert("RGBA")
    result_img = Image.new("RGBA", base_img.size, (0, 0, 0, 0))
    for x in range(base_img.width):
        for y in range(base_img.height):
            base_pixel = base_img.getpixel((x, y))
            if base_pixel[3] == 0:
                result_img.putpixel((x, y), base_pixel)
            else:
                overlay_pixel = overlay_img.getpixel((x, y))
                alpha = overlay_pixel[3] / 255.0
                new_pixel = (
                    int((1 - alpha) * base_pixel[0] + alpha * overlay_pixel[0]),
                    int((1 - alpha) * base_pixel[1] + alpha * overlay_pixel[1]),
                    int((1 - alpha) * base_pixel[2] + alpha * overlay_pixel[2]),
                    base_pixel[3]
                )
                result_img.putpixel((x, y), new_pixel)
    result_img.save(argv[4]+".png")
print("Done")
