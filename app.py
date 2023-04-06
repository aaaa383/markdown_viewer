import streamlit as st
import base64
import io
import markdown


def markdown_to_html(md_text):
    return markdown.markdown(md_text, extensions=["tables", "fenced_code", "codehilite"])


st.title("Markdownファイルアップロードアプリ")

uploaded_file = st.file_uploader(
    "Markdownファイルをアップロードしてください", type=["md", "markdown"])

if uploaded_file is not None:
    file_contents = uploaded_file.read().decode("utf-8")
    html_contents = markdown_to_html(file_contents)
    st.write(html_contents, unsafe_allow_html=True)
else:
    st.write("アップロードされたファイルはありません。")
