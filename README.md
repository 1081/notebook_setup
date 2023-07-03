# notebook_setup

Tools to setup and configure jupyter notebooks (ipynb files) with line and cell magic

## Install

```python
from notebook_setup import notebook_setup, notebook_config_plotly_rendering
```

## Usage

### Notebook setup

```python
notebook_setup(autoreload=True, background_transparent=True)
```

`autoreload=True` runs this line magic:

```
%load_ext autoreload
%autoreload 2
```

`background_transparent=True` runs this cell magic:

```
%%html
<style>
.cell-output-ipywidget-background {background-color: transparent !important;}
.jp-OutputArea-output {background-color: transparent;}
</style>
```

### Configure the behavior of Plotly figures in Jupyter notebooks

```python
notebook_config_plotly_rendering(
    force_small_file=True,
    global_renderer="svg",
    verbose=True,
)
```

Only figures with `fig.show()` are effected by this configuration.

`force_small_file=True`:  Plotly figures are not saved inside the notebook.

`global_renderer: str =`"[available options](https://plotly.com/python/renderers/)": Specifies render format, has only an effect if `force_small_file=False`

### Configuration examples

**Develop notebooks** minimal file size, saves large notebooks very quickly on disc:

```python
notebook_config_plotly_rendering(force_small_file=True, global_renderer="svg")
```

**Archive notebooks on disk**  large file size, stores interactive figures, uses default renderer

```python
notebook_config_plotly_rendering(force_small_file=False, global_renderer=None)
```

**Export as html or push to GitHub**  small file size, vector or raster images depending on selected renderer

```python
notebook_config_plotly_rendering(force_small_file=False, global_renderer="svg")
```

**Configure individual figures**  independent of setting of `global_renderer`

```python
fig.show(renderer="browser")
```

Hint: `"browser"` opens a figure in your web browser, you have bigger window compared to a notebook cell
