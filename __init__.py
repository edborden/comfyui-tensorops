from .nodes import NODE_CLASS_MAPPINGS as NODE_CLASS_MAPPINGS_ORIGINAL
from .nodes import NODE_DISPLAY_NAME_MAPPINGS as NODE_DISPLAY_NAME_MAPPINGS_ORIGINAL

# Import the renamed nodes directly
from .nodes.sam2_nodes import TensorOps_DownloadAndLoadSAM2Model, TensorOps_Sam2Segmentation, TensorOps_Florence2toCoordinates, TensorOps_Sam2VideoSegmentationAddPoints, TensorOps_Sam2VideoSegmentation, TensorOps_Sam2AutoSegmentation
from .nodes.florence import TensorOps_DownloadAndLoadFlorence2Model, TensorOps_Florence2Run

# Create mappings for backward compatibility
NODE_CLASS_MAPPINGS = {
    **NODE_CLASS_MAPPINGS_ORIGINAL,
    # Add original node names mapped to the new classes for backward compatibility
    "DownloadAndLoadSAM2Model": TensorOps_DownloadAndLoadSAM2Model,
    "Sam2Segmentation": TensorOps_Sam2Segmentation,
    "Florence2toCoordinates": TensorOps_Florence2toCoordinates,
    "Sam2VideoSegmentationAddPoints": TensorOps_Sam2VideoSegmentationAddPoints,
    "Sam2VideoSegmentation": TensorOps_Sam2VideoSegmentation,
    "Sam2AutoSegmentation": TensorOps_Sam2AutoSegmentation,
    "DownloadAndLoadFlorence2Model": TensorOps_DownloadAndLoadFlorence2Model,
    "Florence2Run": TensorOps_Florence2Run,
}

# Create display name mappings
NODE_DISPLAY_NAME_MAPPINGS = {
    **NODE_DISPLAY_NAME_MAPPINGS_ORIGINAL,
    # Add original node names with their display names
    "DownloadAndLoadSAM2Model": "(Down)Load SAM2Model",
    "Sam2Segmentation": "Sam2Segmentation",
    "Florence2toCoordinates": "Florence2 Coordinates",
    "Sam2VideoSegmentationAddPoints": "Sam2VideoSegmentationAddPoints",
    "Sam2VideoSegmentation": "Sam2VideoSegmentation",
    "Sam2AutoSegmentation": "Sam2AutoSegmentation",
    "DownloadAndLoadFlorence2Model": "DownloadAndLoadFlorence2Model",
    "Florence2Run": "Florence2Run",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
