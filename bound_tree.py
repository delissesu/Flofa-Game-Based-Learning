import cairo

# Define canvas dimensions (from cell ea5627f2)
WIDTH = 600
HEIGHT = 800

# Create a Pycairo image surface (from cell ea5627f2)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)

# Create a cairo context (from cell ea5627f2)
context = cairo.Context(surface)

# --- Tree Trunk Drawing (from cell 0aa80f52) ---

# Define trunk colors
dark_brown = (88/255, 60/255, 34/255)
medium_brown = (120/255, 80/255, 45/255)
light_brown = (150/255, 100/255, 60/255)

context.save()

context.set_source_rgb(*medium_brown)
context.move_to(WIDTH * 0.45, HEIGHT * 0.9)
context.curve_to(WIDTH * 0.4, HEIGHT * 0.7, WIDTH * 0.48, HEIGHT * 0.5, WIDTH * 0.5, HEIGHT * 0.45)
context.curve_to(WIDTH * 0.52, HEIGHT * 0.5, WIDTH * 0.6, HEIGHT * 0.7, WIDTH * 0.55, HEIGHT * 0.9)
context.close_path()
context.fill()

context.set_source_rgb(*dark_brown)
context.move_to(WIDTH * 0.5, HEIGHT * 0.45)
context.curve_to(WIDTH * 0.52, HEIGHT * 0.5, WIDTH * 0.6, HEIGHT * 0.7, WIDTH * 0.55, HEIGHT * 0.9)
context.line_to(WIDTH * 0.49, HEIGHT * 0.9)
context.curve_to(WIDTH * 0.58, HEIGHT * 0.7, WIDTH * 0.5, HEIGHT * 0.5, WIDTH * 0.49, HEIGHT * 0.46)
context.close_path()
context.fill()

context.set_source_rgb(*light_brown)
context.move_to(WIDTH * 0.45, HEIGHT * 0.9)
context.curve_to(WIDTH * 0.42, HEIGHT * 0.8, WIDTH * 0.45, HEIGHT * 0.6, WIDTH * 0.48, HEIGHT * 0.48)
context.line_to(WIDTH * 0.49, HEIGHT * 0.5)
context.curve_to(WIDTH * 0.47, HEIGHT * 0.6, WIDTH * 0.44, HEIGHT * 0.8, WIDTH * 0.47, HEIGHT * 0.9)
context.close_path()
context.fill()

context.restore()

# --- Tree Trunk Details (from cell c1c99fcb) ---

dark_brown_detail = (70/255, 48/255, 20/255)
light_brown_detail = (170/255, 115/255, 75/255)

context.save()

context.set_source_rgb(*dark_brown_detail)
context.set_line_width(2)

context.move_to(WIDTH * 0.51, HEIGHT * 0.55)
context.line_to(WIDTH * 0.53, HEIGHT * 0.65)
context.line_to(WIDTH * 0.52, HEIGHT * 0.75)
context.stroke()

context.move_to(WIDTH * 0.47, HEIGHT * 0.6)
context.line_to(WIDTH * 0.46, HEIGHT * 0.7)
context.stroke()

context.set_source_rgb(*light_brown_detail)
context.set_line_width(1.5)

context.move_to(WIDTH * 0.48, HEIGHT * 0.5)
context.line_to(WIDTH * 0.46, HEIGHT * 0.6)
context.stroke()

context.move_to(WIDTH * 0.50, HEIGHT * 0.68)
context.line_to(WIDTH * 0.49, HEIGHT * 0.78)
context.stroke()

context.set_source_rgb(*light_brown)
context.move_to(WIDTH * 0.49, HEIGHT * 0.45)
context.curve_to(WIDTH * 0.495, HEIGHT * 0.448, WIDTH * 0.505, HEIGHT * 0.448, WIDTH * 0.51, HEIGHT * 0.45)
context.set_line_width(1)
context.stroke()

context.restore()

# --- Foliage Drawing (from cell 892fb895) ---

dark_green = (30/255, 70/255, 20/255)
medium_green = (70/255, 120/255, 40/255)
light_green = (120/255, 180/255, 70/255)

context.save()

context.set_source_rgb(*medium_green)
context.move_to(WIDTH * 0.3, HEIGHT * 0.35)
context.curve_to(WIDTH * 0.2, HEIGHT * 0.2, WIDTH * 0.4, HEIGHT * 0.15, WIDTH * 0.5, HEIGHT * 0.2)
context.curve_to(WIDTH * 0.6, HEIGHT * 0.25, WIDTH * 0.45, HEIGHT * 0.4, WIDTH * 0.3, HEIGHT * 0.35)
context.fill()

context.set_source_rgb(*medium_green)
context.move_to(WIDTH * 0.5, HEIGHT * 0.2)
context.curve_to(WIDTH * 0.6, HEIGHT * 0.15, WIDTH * 0.8, HEIGHT * 0.25, WIDTH * 0.7, HEIGHT * 0.4)
context.curve_to(WIDTH * 0.6, HEIGHT * 0.45, WIDTH * 0.55, HEIGHT * 0.3, WIDTH * 0.5, HEIGHT * 0.2)
context.fill()

context.set_source_rgb(*medium_green)
context.move_to(WIDTH * 0.25, HEIGHT * 0.45)
context.curve_to(WIDTH * 0.15, HEIGHT * 0.35, WIDTH * 0.35, HEIGHT * 0.3, WIDTH * 0.45, HEIGHT * 0.4)
context.curve_to(WIDTH * 0.4, HEIGHT * 0.5, WIDTH * 0.3, HEIGHT * 0.5, WIDTH * 0.25, HEIGHT * 0.45)
context.fill()

context.set_source_rgb(*medium_green)
context.move_to(WIDTH * 0.75, HEIGHT * 0.45)
context.curve_to(WIDTH * 0.85, HEIGHT * 0.35, WIDTH * 0.65, HEIGHT * 0.3, WIDTH * 0.55, HEIGHT * 0.4)
context.curve_to(WIDTH * 0.6, HEIGHT * 0.5, WIDTH * 0.7, HEIGHT * 0.5, WIDTH * 0.75, HEIGHT * 0.45)
context.fill()

context.set_source_rgb(*dark_green)

context.move_to(WIDTH * 0.4, HEIGHT * 0.3)
context.curve_to(WIDTH * 0.45, HEIGHT * 0.35, WIDTH * 0.3, HEIGHT * 0.4, WIDTH * 0.28, HEIGHT * 0.38)
context.curve_to(WIDTH * 0.35, HEIGHT * 0.32, WIDTH * 0.4, HEIGHT * 0.3, WIDTH * 0.4, HEIGHT * 0.3)
context.fill()

context.move_to(WIDTH * 0.6, HEIGHT * 0.3)
context.curve_to(WIDTH * 0.65, HEIGHT * 0.35, WIDTH * 0.7, HEIGHT * 0.4, WIDTH * 0.68, HEIGHT * 0.38)
context.curve_to(WIDTH * 0.65, HEIGHT * 0.32, WIDTH * 0.6, HEIGHT * 0.3, WIDTH * 0.6, HEIGHT * 0.3)
context.fill()

context.move_to(WIDTH * 0.45, HEIGHT * 0.4)
context.curve_to(WIDTH * 0.5, HEIGHT * 0.35, WIDTH * 0.55, HEIGHT * 0.4, WIDTH * 0.5, HEIGHT * 0.45)
context.close_path()
context.fill()

context.move_to(WIDTH * 0.7, HEIGHT * 0.4)
context.curve_to(WIDTH * 0.75, HEIGHT * 0.45, WIDTH * 0.65, HEIGHT * 0.5, WIDTH * 0.6, HEIGHT * 0.45)
context.close_path()
context.fill()

context.set_source_rgb(*light_green)

context.move_to(WIDTH * 0.35, HEIGHT * 0.25)
context.curve_to(WIDTH * 0.28, HEIGHT * 0.2, WIDTH * 0.38, HEIGHT * 0.18, WIDTH * 0.42, HEIGHT * 0.22)
context.curve_to(WIDTH * 0.38, HEIGHT * 0.26, WIDTH * 0.35, HEIGHT * 0.25, WIDTH * 0.35, HEIGHT * 0.25)
context.fill()

context.move_to(WIDTH * 0.55, HEIGHT * 0.25)
context.curve_to(WIDTH * 0.5, HEIGHT * 0.2, WIDTH * 0.6, HEIGHT * 0.18, WIDTH * 0.65, HEIGHT * 0.22)
context.curve_to(WIDTH * 0.6, HEIGHT * 0.26, WIDTH * 0.55, HEIGHT * 0.25, WIDTH * 0.55, HEIGHT * 0.25)
context.fill()

context.move_to(WIDTH * 0.3, HEIGHT * 0.4)
context.curve_to(WIDTH * 0.25, HEIGHT * 0.35, WIDTH * 0.35, HEIGHT * 0.33, WIDTH * 0.38, HEIGHT * 0.38)
context.curve_to(WIDTH * 0.35, HEIGHT * 0.41, WIDTH * 0.3, HEIGHT * 0.4, WIDTH * 0.3, HEIGHT * 0.4)
context.fill()

context.restore()

# --- Foliage Details (from cell f431fc20) ---

darker_green_detail = (20/255, 60/255, 15/255)
brighter_green_detail = (140/255, 200/255, 90/255)

context.save()

context.set_source_rgb(*darker_green_detail)

context.move_to(WIDTH * 0.48, HEIGHT * 0.25)
context.curve_to(WIDTH * 0.5, HEIGHT * 0.3, WIDTH * 0.52, HEIGHT * 0.25, WIDTH * 0.5, HEIGHT * 0.2)
context.close_path()
context.fill()

context.move_to(WIDTH * 0.65, HEIGHT * 0.45)
context.curve_to(WIDTH * 0.7, HEIGHT * 0.48, WIDTH * 0.75, HEIGHT * 0.4, WIDTH * 0.7, HEIGHT * 0.35)
context.curve_to(WIDTH * 0.68, HEIGHT * 0.43, WIDTH * 0.65, HEIGHT * 0.45, WIDTH * 0.65, HEIGHT * 0.45)
context.fill()

context.set_source_rgb(*brighter_green_detail)

context.move_to(WIDTH * 0.33, HEIGHT * 0.22)
context.curve_to(WIDTH * 0.28, HEIGHT * 0.18, WIDTH * 0.35, HEIGHT * 0.15, WIDTH * 0.4, HEIGHT * 0.18)
context.curve_to(WIDTH * 0.37, HEIGHT * 0.21, WIDTH * 0.33, HEIGHT * 0.22, WIDTH * 0.33, HEIGHT * 0.22)
context.fill()

context.move_to(WIDTH * 0.58, HEIGHT * 0.18)
context.curve_to(WIDTH * 0.53, HEIGHT * 0.15, WIDTH * 0.65, HEIGHT * 0.15, WIDTH * 0.7, HEIGHT * 0.22)
context.curve_to(WIDTH * 0.65, HEIGHT * 0.2, WIDTH * 0.58, HEIGHT * 0.18, WIDTH * 0.58, HEIGHT * 0.18)
context.fill()

context.move_to(WIDTH * 0.28, HEIGHT * 0.42)
context.curve_to(WIDTH * 0.2, HEIGHT * 0.38, WIDTH * 0.3, HEIGHT * 0.35, WIDTH * 0.35, HEIGHT * 0.38)
context.curve_to(WIDTH * 0.32, HEIGHT * 0.41, WIDTH * 0.28, HEIGHT * 0.42, WIDTH * 0.28, HEIGHT * 0.42)
context.fill()

context.restore()

# --- Save Image (original code) ---
output_filename = "clash_of_clans_tree.png"
surface.write_to_png(output_filename)
print(f"Image saved successfully as {output_filename}")