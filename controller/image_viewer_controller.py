

class ImageViewerController():
    def __init__(self,image_viewer):
        self.image_viewer = image_viewer

    def plot_image(self):
        # height, width = self.imgByte.shape
        # image_view_widget.getView().setLimits(xMin=0, xMax=width, yMin=0, yMax=height)
        self.image_viewer.image_view_widget.setImage(self.image_viewer.image_object.imgByte)
        self.select_ft_component()

    def select_ft_component(self):
        selected_text = self.image_viewer.ft_components_combobox.currentText()
        match selected_text:
            case "FT Magnitude":
                self.show_magnitude_components()

            case "FT Phase":
                self.show_phase_components()

            case "FT Imaginary":
                self.show_imaginary_components()

            case "FT Real":
                self.show_real_components()
            case _:
                return
    
    def show_magnitude_components(self):
        self.image_viewer.ft_viewer.setImage(self.image_viewer.image_object.magnitudePlot)

    def show_phase_components(self):
        self.image_viewer.ft_viewer.setImage(self.image_viewer.image_object.phasePlot)


    def show_imaginary_components(self):
        self.image_viewer.ft_viewer.setImage(self.image_viewer.image_object.imaginaryPlot)


    def show_real_components(self):
        self.image_viewer.ft_viewer.setImage(self.image_viewer.image_object.realPlot)


    