from IPython import get_ipython
from IPython.display import HTML, display


def notebook_setup(autoreload=True, background_transparent=True):
    """Import this function a jupyter notebook and run it to config the notebook with magic commands"""

    if autoreload:
        get_ipython().run_line_magic("load_ext", "autoreload")
        get_ipython().run_line_magic("autoreload", "2")

    if background_transparent:
        get_ipython().run_cell_magic(
            "html",
            "",  # NOTE not a specific cell
            """
            <style>
            .cell-output-ipywidget-background {background-color: transparent !important;}
            .jp-OutputArea-output {background-color: transparent;}
            </style>
            """,
        )


def notebook_config_plotly_rendering(
    force_small_file: bool = True,
    global_renderer: str = None,
):
    """
    Configures the behavior of Plotly figures in Jupyter notebooks. -> Make small files and render on GitHub.
    Only figures with fig.show() are effected by this configuration.
    This function monkey patches (modifies at runtime) behavior of fig.show(). Tested with VS Code.

    Args:
        force_small_file: If True, Plotly figures are not saved inside the notebook.
        global_renderer (str, optional): Specifies a custom global renderer for the figures.
            - None: Default renderer (depending on environment)
            - "svg": static vector plot (small file)
            - "png": static raster plot (small file)
            - "notebook"
            - "vscode"
            - "browser": opens all plots in a browser window
            for more options see: https://plotly.com/python/renderers/

    Hints:
    - To "overwrite" force_small_file for an individual figure, specify a renderer:
        fig.show(renderer="notebook")

    - To open a plot in the browser (bigger window than notebook cell):
        fig.show(renderer="browser")

    - To save the notebook with static images:
        These images are displayed on GitHub and in HTML exports without creating large files.
        notebook_config_plotly_rendering(force_small_file=False, custom_renderer="svg")
    """
    import plotly.io as pio
    from plotly.basedatatypes import BaseFigure

    if force_small_file:

        def show(self, *args, renderer=None, **kwargs):
            "Monkey patch plotly fig.show()"
            if renderer:
                return pio.show(self, *args, renderer=renderer, **kwargs)
            else:
                display(
                    self,
                    # raw=True,
                )

        # msg = f"""global_renderer="{global_renderer}" has no effect, set force_small_file=False"""
        # display(HTML(f"""<span style="color:red">Warning: </span>{msg}"""))

    else:
        if global_renderer:
            pio.renderers.default = global_renderer

        def show(self, *args, **kwargs):
            "Plotly default implementation"
            return pio.show(self, *args, **kwargs)

    BaseFigure.show = show
