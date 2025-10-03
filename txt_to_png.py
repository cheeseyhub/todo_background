from PIL import Image, ImageDraw, ImageFont

def convert_txt_to_png(
        input_txt_file: str ,
        output_png_file:str, 
        font_path=None,
        font_size=20,
        text_color=(255,255,255),
        background_color=(0,0,0),
        image_size=(1366,768)):

        text = ''
        try:
            with open(input_txt_file, 'r') as file:
                text = file.read();
        except FileNotFoundError:
             print(f"File {input_txt_file} not found.")
             return

        
        image = Image.new('RGB', image_size, color=background_color);

        #Load the font
        font = ImageFont.load_default();
        try:
            font = ImageFont.truetype(font_path if font_path else "arial.ttf", font_size);
        except IOError:
            print("Font file not found. Using default font.");
            font = ImageFont.load_default();

        
        text_pos = (image_size[0]/2, image_size[1]/2);
        text_color = text_color;
        draw = ImageDraw.Draw(image);
        draw.text(text_pos,text,font=font,fill=text_color);
        image.save(output_png_file);

        print("-----------------------");
        print("Conversion complete.");
        print(f"Saved image to {output_png_file}");
        print("-----------------------");




convert_txt_to_png("todo.txt","./background/todo.png",font_size=200);