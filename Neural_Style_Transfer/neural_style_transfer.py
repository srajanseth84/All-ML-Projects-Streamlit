import streamlit as st
import os
import tensorflow_hub as hub
from Neural_Style_Transfer.utils import load_img, transform_img, tensor_to_image, imshow
import tensorflow as tf

def app():

    st.title("Neural Style Transfer 🖼")

    st.write('Neural Style Transfer is a technique that uses deep learning to compose one image in the style of another image. Have your ever wished you could paint like Picasso or Van Gogh? This is your chance! \n')
    st.write("To know more about this app, visit [**GitHub**](https://github.com/srajanseth84/Neural-Style-Transfer)")

    @st.cache(allow_output_mutation=True)
    def load_model():
        hub_model = hub.load(
            'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
        return hub_model

    model_load_state = st.text('Loading Model...')
    model = load_model()

    # Notify the reader that the data was successfully loaded.
    model_load_state.text('Loading Model...done!')

    content_image, style_image = st.columns(2)
    try:
        with content_image:
            st.write('## Content Image...')
            chosen_content = st.radio(
                '  ',
                ("Upload", "URL"))
            if chosen_content == 'Upload':
                st.write(f"You choosed {chosen_content}!")
                content_image_file = st.file_uploader(
                    "Pick a Content image", type=("png", "jpg"))
                try:
                    content_image_file = content_image_file.read()
                    content_image_file = transform_img(content_image_file)
                except:
                    pass
            elif chosen_content == 'URL':
                st.write(f"You choosed {chosen_content}!")
                url = st.text_input('URL for the content image.')
                try:
                    content_path = tf.keras.utils.get_file(
                        os.path.join(os.getcwd(), 'content.jpg'), url)
                except:
                    pass
                try:
                    content_image_file = load_img(content_path)

                except:
                    pass
            try:
                st.write('Content Image...')
                st.image(imshow(content_image_file))
            except:
                pass

        with style_image:
            st.write('## Style Image...')
            chosen_style = st.radio(
                ' ',
                ("Choose from List", "Upload", "URL"))
            if chosen_style == 'Choose from List':
                try:
                    # Delete style.jpg before setting
                    os.remove("style.jpg")
                except:
                    pass
                st.write(f"You choosed to Select from List!")
                select = st.selectbox('List', ('Starry night', 'Clocks', 'Picasso Portret', 'Mona Lisa',
                                               'The Kiss by Klimt', 'Birth of Venus', 'Church in Auvers', 'Sejalec',
                                               'The Scream', 'Kofetarica',))

                if select == 'Starry night':
                    url = 'https://media.overstockart.com/optimized/cache/data/product_images/VG485-1000x1000.jpg'
                elif select == 'Clocks':
                    url = 'https://upload.wikimedia.org/wikipedia/en/d/dd/The_Persistence_of_Memory.jpg'
                elif select == 'Picasso Portret':
                    url = 'https://images.saatchiart.com/saatchi/1311333/art/6500245/5569923-AOAGHVQR-7.jpg'
                elif select == 'Mona Lisa':
                    url = 'https://cdn.cnn.com/cnnnext/dam/assets/190430171751-mona-lisa.jpg'
                elif select == 'The Kiss by Klimt':
                    url = 'https://i.pinimg.com/originals/46/44/7b/46447b35c81b2d750d29e27f7738a6a6.jpg'
                elif select == 'Birth of Venus':
                    url = 'https://art-sheep.com/wp-content/uploads/2019/06/Sandro-Botticelli-Birth-of-Venus-1024x683.jpg'
                elif select == 'Church in Auvers':
                    url = 'https://cdn.theculturetrip.com/wp-content/uploads/2019/01/vincent_van_gogh_-_the_church_in_auvers-sur-oise_view_from_the_chevet_-_google_art_project.jpg'
                elif select == 'The Scream':
                    url = 'https://upload.wikimedia.org/wikipedia/commons/9/9d/The_Scream_by_Edvard_Munch%2C_1893_-_Nasjonalgalleriet.png'
                elif select == 'Kofetarica':
                    url = 'https://upload.wikimedia.org/wikipedia/commons/6/61/Ivana_Kobilca_-_Kofetarica.jpg'
                elif select == 'Sejalec':
                    url = 'https://www.bolha.com/image-bigger/slike-umetnine-starine/slika-sejalec-lilijana-levstik-olje-platno-slika-15130001.jpg'

                try:
                    style_path = tf.keras.utils.get_file(
                        os.path.join(os.getcwd(), 'style.jpg'), url)
                except:
                    pass
                try:
                    style_image_file = load_img(style_path)

                except:
                    pass

            elif chosen_style == 'Upload':
                st.write(f"You choosed {chosen_style}!")
                style_image_file = st.file_uploader(
                    "Pick a Style image", type=("png", "jpg"))
                try:
                    style_image_file = style_image_file.read()
                    style_image_file = transform_img(style_image_file)
                except:
                    pass
            elif chosen_style == 'URL':
                st.write(f"You choosed {chosen_style}!")
                url = st.text_input('URL for the style image.')
                try:
                    style_path = tf.keras.utils.get_file(
                        os.path.join(os.getcwd(), 'style.jpg'), url)
                except:
                    pass
                try:
                    style_image_file = load_img(style_path)

                except:
                    pass
            try:
                st.write('Style Image...')
                st.image(imshow(style_image_file))
            except:
                pass

        predict = st.button('Transfering Style 🖼')

        if predict:
            try:
                stylized_image = model(tf.constant(
                    content_image_file), tf.constant(style_image_file))[0]

                final_image = tensor_to_image(stylized_image)
            except:
                stylized_image = model(tf.constant(
                    tf.convert_to_tensor(content_image_file[:, :, :, :3])
                ),
                    tf.constant(
                        tf.convert_to_tensor(style_image_file[:, :, :, :3])
                    )
                )[0]

                final_image = tensor_to_image(stylized_image)

            st.write('Resultant Image...')
            st.image(final_image)

            try:
                # Delete style.jpg and content.jpg
                os.remove("style.jpg")
                os.remove("content.jpg")
            except:
                pass
    except:
        st.warning("Some **Unexpected** Error happen")
        st.warning(
            "Please create a **Issue** on [Github](https://github.com/srajanseth84/Neural-Style-Transfer)")

    st.markdown("Created by **Srajan Seth**")
    st.markdown(body="""

    <th style="border:None"><a href="https://www.linkedin.com/in/srajan-seth-8713b3183/" target="blank"><img align="center" src="https://bit.ly/3wCl82U" alt="srajan-seth-8713b3183" height="40" width="40" /></a></th>
    <th style="border:None"><a href="https://github.com/srajanseth84" target="blank"><img align="center" src="https://bit.ly/3c2onZS" alt="srajanseth84" height="40" width="40" /></a></th>

    """, unsafe_allow_html=True)
