import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=900, height=900)

with dpg.window(label="Example Window", no_title_bar=True, no_resize=True, no_move=True):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.set_primary_window("Example Window", True)
dpg.setup_dearpygui()
dpg.show_viewport(maximized=True)
dpg.start_dearpygui()
dpg.destroy_context()