"""Color Palette Generator - Generate harmonious palettes from a seed color."""
import colorsys

def hex_to_hsv(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i+2], 16) / 255 for i in (0, 2, 4))
    return colorsys.rgb_to_hsv(r, g, b)

def hsv_to_hex(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return "#{:02X}{:02X}{:02X}".format(int(r*255), int(g*255), int(b*255))

def complementary(h, s, v):
    return [(h, s, v), ((h + 0.5) % 1, s, v)]

def triadic(h, s, v):
    return [(h, s, v), ((h + 1/3) % 1, s, v), ((h + 2/3) % 1, s, v)]

def analogous(h, s, v, spread=0.083):
    return [(h, s, v), ((h - spread) % 1, s, v), ((h + spread) % 1, s, v)]

def tetradic(h, s, v):
    return [(h, s, v), ((h+0.25)%1, s, v), ((h+0.5)%1, s, v), ((h+0.75)%1, s, v)]

def shades(h, s, v, steps=5):
    return [(h, s, v * i / steps) for i in range(1, steps + 1)]

def print_palette(name, colors):
    hexes = [hsv_to_hex(*c) for c in colors]
    print(f"\n{name}:")
    for hex_c in hexes:
        bar = "█" * 20
        print(f"  {hex_c}  {bar}")
    return hexes

if __name__ == "__main__":
    seed = input("Enter seed color (hex, e.g. #3498db): ").strip() or "#3498db"
    h, s, v = hex_to_hsv(seed)
    print(f"\n🎨 Palettes for {seed}")
    print_palette("Complementary", complementary(h, s, v))
    print_palette("Triadic", triadic(h, s, v))
    print_palette("Analogous", analogous(h, s, v))
    print_palette("Tetradic", tetradic(h, s, v))
    print_palette("Shades", shades(h, s, v))
