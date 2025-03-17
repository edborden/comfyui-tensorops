from .channel_select import ChannelSelector
from .mask_image import MaskImage
from .save_surreal import SaveJsonToSurreal, SaveTextToSurreal
from .fetch_surreal import FetchJsonFromSurreal
from .foreground_mask import ForegroundMask
from .save_to_s3 import SaveImageToS3
from .redis import SaveToRedis, FetchFromRedis
from .fal import FalDifferentialDiffusion, FalDiffusion
from .background_select import BackgroundSelect
from .layer_mask import GetLayerMask
from .stream import SendImageOnWebSocket, SendJsonOnWebSocket
from .separate_mask import SeparateMask
from .face_swap import FaceSwap

# Import the SAM2 and Florence2 nodes
from .sam2_nodes import TensorOps_DownloadAndLoadSAM2Model, TensorOps_Sam2Segmentation, TensorOps_Florence2toCoordinates
from .sam2_nodes import TensorOps_Sam2VideoSegmentationAddPoints, TensorOps_Sam2VideoSegmentation, TensorOps_Sam2AutoSegmentation
from .florence import TensorOps_DownloadAndLoadFlorence2Model, TensorOps_Florence2Run

NODE_CLASS_MAPPINGS = {
    "ChannelSelector": ChannelSelector,
    "MaskImage": MaskImage,
    "SaveImageToS3": SaveImageToS3,
    "SaveJsonToSurreal": SaveJsonToSurreal,
    "SaveTextToSurreal": SaveTextToSurreal,
    "FetchJsonFromSurreal": FetchJsonFromSurreal,
    "ForegroundMask": ForegroundMask,
    "SaveToRedis": SaveToRedis,
    "FetchFromRedis": FetchFromRedis,
    "FalDifferentialDiffusion": FalDifferentialDiffusion,
    "FalDiffusion": FalDiffusion,
    "BackgroundSelect": BackgroundSelect,
    "GetLayerMask": GetLayerMask,
    "SendImageOnWebSocket": SendImageOnWebSocket,
    "SendJsonOnWebSocket": SendJsonOnWebSocket,
    "SeparateMask": SeparateMask,
    "FaceSwap": FaceSwap,
    
    # Add the renamed SAM2 and Florence2 nodes
    "TensorOps_DownloadAndLoadSAM2Model": TensorOps_DownloadAndLoadSAM2Model,
    "TensorOps_Sam2Segmentation": TensorOps_Sam2Segmentation,
    "TensorOps_Florence2toCoordinates": TensorOps_Florence2toCoordinates,
    "TensorOps_Sam2VideoSegmentationAddPoints": TensorOps_Sam2VideoSegmentationAddPoints,
    "TensorOps_Sam2VideoSegmentation": TensorOps_Sam2VideoSegmentation,
    "TensorOps_Sam2AutoSegmentation": TensorOps_Sam2AutoSegmentation,
    "TensorOps_DownloadAndLoadFlorence2Model": TensorOps_DownloadAndLoadFlorence2Model,
    "TensorOps_Florence2Run": TensorOps_Florence2Run
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ChannelSelector":"ChannelSelector",
    "MaskImage": "MaskImage",
    "SaveImageToS3": "SaveImageToS3",
    "SaveJsonToSurreal": "SaveJsonToSurreal",
    "SaveTextToSurreal": "SaveTextToSurreal",
    "FetchJsonFromSurreal": "FetchJsonFromSurreal",
    "ForegroundMask": "ForegroundMask",
    "SaveToRedis": "SaveToRedis",
    "FetchFromRedis": "FetchFromRedis",
    "FalDifferentialDiffusion": "FalDifferentialDiffusion",
    "FalDiffusion": "FalDiffusion",
    "BackgroundSelect": "BackgroundSelect",
    "GetLayerMask": "GetLayerMask",
    "SendImageOnWebSocket": "SendImageOnWebSocket",
    "SendJsonOnWebSocket": "SendJsonOnWebSocket",
    "SeparateMask": "SeparateMask",
    "FaceSwap": "FaceSwap",
    
    # Add display names for the renamed nodes
    "TensorOps_DownloadAndLoadSAM2Model": "TensorOps - Download SAM2 Model",
    "TensorOps_Sam2Segmentation": "TensorOps - SAM2 Segmentation",
    "TensorOps_Florence2toCoordinates": "TensorOps - Florence2 to Coordinates",
    "TensorOps_Sam2VideoSegmentationAddPoints": "TensorOps - SAM2 Video Segmentation Add Points",
    "TensorOps_Sam2VideoSegmentation": "TensorOps - SAM2 Video Segmentation",
    "TensorOps_Sam2AutoSegmentation": "TensorOps - SAM2 Auto Segmentation",
    "TensorOps_DownloadAndLoadFlorence2Model": "TensorOps - Download Florence2 Model",
    "TensorOps_Florence2Run": "TensorOps - Florence2 Run"
}
