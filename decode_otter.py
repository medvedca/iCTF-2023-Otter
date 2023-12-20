from PIL import Image
import numpy as np

def calculate_histograms(image_path):
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        r, g, b = img.split()
        
        histogram_r = r.histogram()
        histogram_g = g.histogram()
        histogram_b = b.histogram()
        
        return histogram_r, histogram_g, histogram_b

# radius_d: radius of the color neighborhood for depressed colors
# radius_p: radius of the color neighborhood for pronounced colors
def find_depressed_and_pronounced_colors(histogram, radius_d=3, radius_p=2):
    depressed = []
    pronounced = []
    lower_bound = max(radius_d, radius_p)
    upper_bound = 256 - max(radius_d, radius_p)
    #upper_bound = 200

    for i in range(lower_bound, upper_bound):
        # Neighborhood for depressed colors
        local_values_d = histogram[i-radius_d:i+radius_d+1]

        # Neighborhood for pronounced colors
        local_values_p = histogram[i-radius_p:i+radius_p+1]

        # Check if the current value is a local minimum (depressed)
        if histogram[i] < min(local_values_d[:radius_d] + local_values_d[radius_d+1:]):
            depressed.append(i)

        # Check if the current value is a local maximum (pronounced)
        if histogram[i] > max(local_values_p[:radius_p] + local_values_p[radius_p+1:]):
            pronounced.append(i)

    return depressed, pronounced

def highlight_selected_colors(image_path, selected_colors, retain_original_color=False):
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        data = np.array(img)

        # Check if any channel contains selected colors
        is_selected_pixel = np.any([np.isin(data[:,:,i], selected_colors[i]) for i in range(3)], axis=0)

        # Initialize highlighted_data with black pixels
        highlighted_data = np.zeros_like(data)

        if retain_original_color:
            # Retain the original color of selected pixels
            highlighted_data[is_selected_pixel] = data[is_selected_pixel]
        else:
            # Set selected pixels to white
            highlighted_data[is_selected_pixel] = [255, 255, 255]
        
        highlighted_img = Image.fromarray(highlighted_data.astype(np.uint8))
        return highlighted_img

image_path = 'input-otter-image.bmp'  # Replace with your image file path
histogram_r, histogram_g, histogram_b = calculate_histograms(image_path)

# Find depressed and pronounced colors for each channel
depressed_r, pronounced_r = find_depressed_and_pronounced_colors(histogram_r)
depressed_g, pronounced_g = find_depressed_and_pronounced_colors(histogram_g)
depressed_b, pronounced_b = find_depressed_and_pronounced_colors(histogram_b)

# Print out the extrema of the histograms for each channel 
print("Depressed Red Colors:", depressed_r)
print("Pronounced Red Colors:", pronounced_r)
print("Depressed Green Colors:", depressed_g)
print("Pronounced Green Colors:", pronounced_g)
print("Depressed Blue Colors:", depressed_b)
print("Pronounced Blue Colors:", pronounced_b)

# Resample the image
depressed_colors = [depressed_r, depressed_g, depressed_b]
pronounced_colors = [pronounced_r, pronounced_g, pronounced_b]

highlighted_pronounced = highlight_selected_colors(image_path, pronounced_colors)
highlighted_pronounced.show()  # Display the image
highlighted_pronounced.save('decoded.bmp')
