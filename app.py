import streamlit as st
import os

os.chdir("/Users/samarjayachandran/Desktop/Wack Coding")

st.set_page_config(page_title="Malheureusement le mieux que je peux faire")

st.title("Une petite question")

question = "Passerais-tu la Saint Valentin avec moi ?"
choice = st.radio(
    question,
    options=["Oui", "Yes"],
    index=None  # no default selection
)

st.write("")  # spacer

if choice is None:
    st.info("Ne pas sélectionner une option n'est pas une option")
else:
    st.success(f"T'as sélectionné : {choice}")
    
    # Display image regardless of which option was chosen
    st.image(
        "https://www.streamlineart.com/media/catalog/product/cache/b1287e81dde340276dcae4c8aae7ab0b/D/3/D3540-3860_1.jpg",  # replace with your image filename or URL
        caption="Avec tout mon amour - ton ours",
        use_container_width=True
    )
