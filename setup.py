import setuptools

setuptools.setup(
    name="streamlit_bd_cytoscapejs",
    version="0.0.1",
    author="Mateus Coelho",
    author_email="mateuscco12@gmail.com",
    description="A Streamlit component wrapping Cytoscape.js",
    long_description="""A Streamlit birectional component wrapping the javascript
    library Cytoscape.js, which is a powerfull tool to draw networks (graphs).""",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
