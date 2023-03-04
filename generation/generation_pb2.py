# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
import tensors_pb2 as tensors__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10generation.proto\x12\x07gooseai\x1a\x1cgoogle/protobuf/struct.proto\x1a\rtensors.proto\"/\n\x05Token\x12\x11\n\x04text\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\n\n\x02id\x18\x02 \x01(\rB\x07\n\x05_text\"T\n\x06Tokens\x12\x1e\n\x06tokens\x18\x01 \x03(\x0b\x32\x0e.gooseai.Token\x12\x19\n\x0ctokenizer_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0f\n\r_tokenizer_id\"\xf3\x02\n\x08\x41rtifact\x12\n\n\x02id\x18\x01 \x01(\x04\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.gooseai.ArtifactType\x12\x0c\n\x04mime\x18\x03 \x01(\t\x12\x12\n\x05magic\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x06\x62inary\x18\x05 \x01(\x0cH\x00\x12\x0e\n\x04text\x18\x06 \x01(\tH\x00\x12!\n\x06tokens\x18\x07 \x01(\x0b\x32\x0f.gooseai.TokensH\x00\x12\x33\n\nclassifier\x18\x0b \x01(\x0b\x32\x1d.gooseai.ClassifierParametersH\x00\x12!\n\x06tensor\x18\x0e \x01(\x0b\x32\x0f.tensors.TensorH\x00\x12\r\n\x05index\x18\x08 \x01(\r\x12,\n\rfinish_reason\x18\t \x01(\x0e\x32\x15.gooseai.FinishReason\x12\x0c\n\x04seed\x18\n \x01(\r\x12\x0c\n\x04uuid\x18\x0c \x01(\t\x12\x0c\n\x04size\x18\r \x01(\x04\x42\x06\n\x04\x64\x61taB\x08\n\x06_magic\"N\n\x10PromptParameters\x12\x11\n\x04init\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x13\n\x06weight\x18\x02 \x01(\x02H\x01\x88\x01\x01\x42\x07\n\x05_initB\t\n\x07_weight\"\xaf\x01\n\x06Prompt\x12\x32\n\nparameters\x18\x01 \x01(\x0b\x32\x19.gooseai.PromptParametersH\x01\x88\x01\x01\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12!\n\x06tokens\x18\x03 \x01(\x0b\x32\x0f.gooseai.TokensH\x00\x12%\n\x08\x61rtifact\x18\x04 \x01(\x0b\x32\x11.gooseai.ArtifactH\x00\x42\x08\n\x06promptB\r\n\x0b_parameters\"\xd7\x02\n\x11SamplerParameters\x12\x10\n\x03\x65ta\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x1b\n\x0esampling_steps\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x1c\n\x0flatent_channels\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12 \n\x13\x64ownsampling_factor\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x16\n\tcfg_scale\x18\x05 \x01(\x02H\x04\x88\x01\x01\x12\x1d\n\x10init_noise_scale\x18\x06 \x01(\x02H\x05\x88\x01\x01\x12\x1d\n\x10step_noise_scale\x18\x07 \x01(\x02H\x06\x88\x01\x01\x42\x06\n\x04_etaB\x11\n\x0f_sampling_stepsB\x12\n\x10_latent_channelsB\x16\n\x14_downsampling_factorB\x0c\n\n_cfg_scaleB\x13\n\x11_init_noise_scaleB\x13\n\x11_step_noise_scale\"\x8b\x01\n\x15\x43onditionerParameters\x12 \n\x13vector_adjust_prior\x18\x01 \x01(\tH\x00\x88\x01\x01\x12(\n\x0b\x63onditioner\x18\x02 \x01(\x0b\x32\x0e.gooseai.ModelH\x01\x88\x01\x01\x42\x16\n\x14_vector_adjust_priorB\x0e\n\x0c_conditioner\"j\n\x12ScheduleParameters\x12\x12\n\x05start\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x10\n\x03\x65nd\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x12\n\x05value\x18\x03 \x01(\x02H\x02\x88\x01\x01\x42\x08\n\x06_startB\x06\n\x04_endB\x08\n\x06_value\"\xe4\x01\n\rStepParameter\x12\x13\n\x0bscaled_step\x18\x01 \x01(\x02\x12\x30\n\x07sampler\x18\x02 \x01(\x0b\x32\x1a.gooseai.SamplerParametersH\x00\x88\x01\x01\x12\x32\n\x08schedule\x18\x03 \x01(\x0b\x32\x1b.gooseai.ScheduleParametersH\x01\x88\x01\x01\x12\x32\n\x08guidance\x18\x04 \x01(\x0b\x32\x1b.gooseai.GuidanceParametersH\x02\x88\x01\x01\x42\n\n\x08_samplerB\x0b\n\t_scheduleB\x0b\n\t_guidance\"\x97\x01\n\x05Model\x12\x30\n\x0c\x61rchitecture\x18\x01 \x01(\x0e\x32\x1a.gooseai.ModelArchitecture\x12\x11\n\tpublisher\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61taset\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x02\x12\x18\n\x10semantic_version\x18\x05 \x01(\t\x12\r\n\x05\x61lias\x18\x06 \x01(\t\"\xbc\x01\n\x10\x43utoutParameters\x12*\n\x07\x63utouts\x18\x01 \x03(\x0b\x32\x19.gooseai.CutoutParameters\x12\x12\n\x05\x63ount\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x11\n\x04gray\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x11\n\x04\x62lur\x18\x04 \x01(\x02H\x02\x88\x01\x01\x12\x17\n\nsize_power\x18\x05 \x01(\x02H\x03\x88\x01\x01\x42\x08\n\x06_countB\x07\n\x05_grayB\x07\n\x05_blurB\r\n\x0b_size_power\"=\n\x1aGuidanceScheduleParameters\x12\x10\n\x08\x64uration\x18\x01 \x01(\x02\x12\r\n\x05value\x18\x02 \x01(\x02\"\x97\x02\n\x1aGuidanceInstanceParameters\x12\x1e\n\x06models\x18\x02 \x03(\x0b\x32\x0e.gooseai.Model\x12\x1e\n\x11guidance_strength\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12\x35\n\x08schedule\x18\x04 \x03(\x0b\x32#.gooseai.GuidanceScheduleParameters\x12/\n\x07\x63utouts\x18\x05 \x01(\x0b\x32\x19.gooseai.CutoutParametersH\x01\x88\x01\x01\x12$\n\x06prompt\x18\x06 \x01(\x0b\x32\x0f.gooseai.PromptH\x02\x88\x01\x01\x42\x14\n\x12_guidance_strengthB\n\n\x08_cutoutsB\t\n\x07_prompt\"~\n\x12GuidanceParameters\x12\x30\n\x0fguidance_preset\x18\x01 \x01(\x0e\x32\x17.gooseai.GuidancePreset\x12\x36\n\tinstances\x18\x02 \x03(\x0b\x32#.gooseai.GuidanceInstanceParameters\"n\n\rTransformType\x12.\n\tdiffusion\x18\x01 \x01(\x0e\x32\x19.gooseai.DiffusionSamplerH\x00\x12%\n\x08upscaler\x18\x02 \x01(\x0e\x32\x11.gooseai.UpscalerH\x00\x42\x06\n\x04type\"\xbd\x03\n\x0fImageParameters\x12\x13\n\x06height\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x12\n\x05width\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x0c\n\x04seed\x18\x03 \x03(\r\x12\x14\n\x07samples\x18\x04 \x01(\x04H\x02\x88\x01\x01\x12\x12\n\x05steps\x18\x05 \x01(\x04H\x03\x88\x01\x01\x12.\n\ttransform\x18\x06 \x01(\x0b\x32\x16.gooseai.TransformTypeH\x04\x88\x01\x01\x12*\n\nparameters\x18\x07 \x03(\x0b\x32\x16.gooseai.StepParameter\x12\x36\n\x10masked_area_init\x18\x08 \x01(\x0e\x32\x17.gooseai.MaskedAreaInitH\x05\x88\x01\x01\x12\x31\n\rweight_method\x18\t \x01(\x0e\x32\x15.gooseai.WeightMethodH\x06\x88\x01\x01\x12\x15\n\x08quantize\x18\n \x01(\x08H\x07\x88\x01\x01\x42\t\n\x07_heightB\x08\n\x06_widthB\n\n\x08_samplesB\x08\n\x06_stepsB\x0c\n\n_transformB\x13\n\x11_masked_area_initB\x10\n\x0e_weight_methodB\x0b\n\t_quantize\"J\n\x11\x43lassifierConcept\x12\x0f\n\x07\x63oncept\x18\x01 \x01(\t\x12\x16\n\tthreshold\x18\x02 \x01(\x02H\x00\x88\x01\x01\x42\x0c\n\n_threshold\"\xf4\x01\n\x12\x43lassifierCategory\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x08\x63oncepts\x18\x02 \x03(\x0b\x32\x1a.gooseai.ClassifierConcept\x12\x17\n\nadjustment\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12$\n\x06\x61\x63tion\x18\x04 \x01(\x0e\x32\x0f.gooseai.ActionH\x01\x88\x01\x01\x12\x35\n\x0f\x63lassifier_mode\x18\x05 \x01(\x0e\x32\x17.gooseai.ClassifierModeH\x02\x88\x01\x01\x42\r\n\x0b_adjustmentB\t\n\x07_actionB\x12\n\x10_classifier_mode\"\xb8\x01\n\x14\x43lassifierParameters\x12/\n\ncategories\x18\x01 \x03(\x0b\x32\x1b.gooseai.ClassifierCategory\x12,\n\x07\x65xceeds\x18\x02 \x03(\x0b\x32\x1b.gooseai.ClassifierCategory\x12-\n\x0frealized_action\x18\x03 \x01(\x0e\x32\x0f.gooseai.ActionH\x00\x88\x01\x01\x42\x12\n\x10_realized_action\"]\n\x15InterpolateParameters\x12\x0e\n\x06ratios\x18\x01 \x03(\x02\x12+\n\x04mode\x18\x02 \x01(\x0e\x32\x18.gooseai.InterpolateModeH\x00\x88\x01\x01\x42\x07\n\x05_mode\"\x9c\x03\n\x14TransformColorAdjust\x12\x17\n\nbrightness\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x15\n\x08\x63ontrast\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x10\n\x03hue\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x17\n\nsaturation\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12\x16\n\tlightness\x18\x05 \x01(\x02H\x04\x88\x01\x01\x12+\n\x0bmatch_image\x18\x06 \x01(\x0b\x32\x11.gooseai.ArtifactH\x05\x88\x01\x01\x12\x30\n\nmatch_mode\x18\x07 \x01(\x0e\x32\x17.gooseai.ColorMatchModeH\x06\x88\x01\x01\x12\x19\n\x0cnoise_amount\x18\x08 \x01(\x02H\x07\x88\x01\x01\x12\x17\n\nnoise_seed\x18\t \x01(\rH\x08\x88\x01\x01\x42\r\n\x0b_brightnessB\x0b\n\t_contrastB\x06\n\x04_hueB\r\n\x0b_saturationB\x0c\n\n_lightnessB\x0e\n\x0c_match_imageB\r\n\x0b_match_modeB\x0f\n\r_noise_amountB\r\n\x0b_noise_seed\"\x8c\x01\n\x12TransformDepthCalc\x12\x19\n\x0c\x62lend_weight\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x18\n\x0b\x62lur_radius\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x14\n\x07reverse\x18\x03 \x01(\x08H\x02\x88\x01\x01\x42\x0f\n\r_blend_weightB\x0e\n\x0c_blur_radiusB\n\n\x08_reverse\"#\n\x0fTransformMatrix\x12\x10\n\x04\x64\x61ta\x18\x01 \x03(\x02\x42\x02\x10\x01\"\x86\x02\n\x11TransformResample\x12(\n\x0b\x62order_mode\x18\x01 \x01(\x0e\x32\x13.gooseai.BorderMode\x12+\n\ttransform\x18\x02 \x01(\x0b\x32\x18.gooseai.TransformMatrix\x12\x35\n\x0eprev_transform\x18\x03 \x01(\x0b\x32\x18.gooseai.TransformMatrixH\x00\x88\x01\x01\x12\x17\n\ndepth_warp\x18\x04 \x01(\x02H\x01\x88\x01\x01\x12\x18\n\x0b\x65xport_mask\x18\x05 \x01(\x08H\x02\x88\x01\x01\x42\x11\n\x0f_prev_transformB\r\n\x0b_depth_warpB\x0e\n\x0c_export_mask\"F\n\x1aPointCloudRenderParameters\x12\x0e\n\x06radius\x18\x01 \x01(\x02\x12\x18\n\x10points_per_pixel\x18\x02 \x01(\r\"-\n\x14MeshRenderParameters\x12\x15\n\rmax_mesh_edge\x18\x01 \x01(\x02\"\xa7\x01\n\x10RenderParameters\x12\x44\n\x15pointcloud_parameters\x18\x01 \x01(\x0b\x32#.gooseai.PointCloudRenderParametersH\x00\x12\x38\n\x0fmesh_parameters\x18\x02 \x01(\x0b\x32\x1d.gooseai.MeshRenderParametersH\x00\x42\x13\n\x11render_parameters\"}\n\x10\x43\x61meraParameters\x12(\n\x0b\x63\x61mera_type\x18\x01 \x01(\x0e\x32\x13.gooseai.CameraType\x12\x12\n\nnear_plane\x18\x02 \x01(\x02\x12\x11\n\tfar_plane\x18\x03 \x01(\x02\x12\x10\n\x03\x66ov\x18\x04 \x01(\x02H\x00\x88\x01\x01\x42\x06\n\x04_fov\"\x8e\x02\n\x13TransformCameraPose\x12\x36\n\x14world_to_view_matrix\x18\x01 \x01(\x0b\x32\x18.gooseai.TransformMatrix\x12\x34\n\x11\x63\x61mera_parameters\x18\x02 \x01(\x0b\x32\x19.gooseai.CameraParameters\x12:\n\x17image_render_parameters\x18\x03 \x01(\x0b\x32\x19.gooseai.RenderParameters\x12\x39\n\x16mask_render_parameters\x18\x04 \x01(\x0b\x32\x19.gooseai.RenderParameters\x12\x12\n\ndo_prefill\x18\x05 \x01(\x08\"\xf1\x01\n\x13TransformParameters\x12\x35\n\x0c\x63olor_adjust\x18\x02 \x01(\x0b\x32\x1d.gooseai.TransformColorAdjustH\x00\x12\x31\n\ndepth_calc\x18\x04 \x01(\x0b\x32\x1b.gooseai.TransformDepthCalcH\x00\x12.\n\x08resample\x18\x05 \x01(\x0b\x32\x1a.gooseai.TransformResampleH\x00\x12\x33\n\x0b\x63\x61mera_pose\x18\x06 \x01(\x0b\x32\x1c.gooseai.TransformCameraPoseH\x00\x42\x0b\n\ttransform\"k\n\x0f\x41ssetParameters\x12$\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x14.gooseai.AssetAction\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x1e\n\x03use\x18\x03 \x01(\x0e\x32\x11.gooseai.AssetUse\"\x94\x01\n\nAnswerMeta\x12\x13\n\x06gpu_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x63pu_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07node_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tengine_id\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\t\n\x07_gpu_idB\t\n\x07_cpu_idB\n\n\x08_node_idB\x0c\n\n_engine_id\"\xa9\x01\n\x06\x41nswer\x12\x11\n\tanswer_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12\x10\n\x08received\x18\x03 \x01(\x04\x12\x0f\n\x07\x63reated\x18\x04 \x01(\x04\x12&\n\x04meta\x18\x06 \x01(\x0b\x32\x13.gooseai.AnswerMetaH\x00\x88\x01\x01\x12$\n\tartifacts\x18\x07 \x03(\x0b\x32\x11.gooseai.ArtifactB\x07\n\x05_meta\"A\n\x0b\x41nswerBatch\x12\x10\n\x08\x62\x61tch_id\x18\x01 \x01(\t\x12 \n\x07\x61nswers\x18\x02 \x03(\x0b\x32\x0f.gooseai.Answer\"\x8f\x04\n\x07Request\x12\x11\n\tengine_id\x18\x01 \x01(\t\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12-\n\x0erequested_type\x18\x03 \x01(\x0e\x32\x15.gooseai.ArtifactType\x12\x1f\n\x06prompt\x18\x04 \x03(\x0b\x32\x0f.gooseai.Prompt\x12)\n\x05image\x18\x05 \x01(\x0b\x32\x18.gooseai.ImageParametersH\x00\x12\x33\n\nclassifier\x18\x07 \x01(\x0b\x32\x1d.gooseai.ClassifierParametersH\x00\x12)\n\x05\x61sset\x18\x08 \x01(\x0b\x32\x18.gooseai.AssetParametersH\x00\x12\x35\n\x0binterpolate\x18\x0b \x01(\x0b\x32\x1e.gooseai.InterpolateParametersH\x00\x12\x31\n\ttransform\x18\x0c \x01(\x0b\x32\x1c.gooseai.TransformParametersH\x00\x12\x38\n\x0b\x63onditioner\x18\x06 \x01(\x0b\x32\x1e.gooseai.ConditionerParametersH\x01\x88\x01\x01\x12-\n\x06\x65xtras\x18\xff\x0f \x01(\x0b\x32\x17.google.protobuf.StructH\x02\x88\x01\x01\x42\x08\n\x06paramsB\x0e\n\x0c_conditionerB\t\n\x07_extrasJ\x04\x08\t\x10\nJ\x04\x08\n\x10\x0b\"w\n\x08OnStatus\x12%\n\x06reason\x18\x01 \x03(\x0e\x32\x15.gooseai.FinishReason\x12\x13\n\x06target\x18\x02 \x01(\tH\x00\x88\x01\x01\x12$\n\x06\x61\x63tion\x18\x03 \x03(\x0e\x32\x14.gooseai.StageActionB\t\n\x07_target\"\\\n\x05Stage\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x07request\x18\x02 \x01(\x0b\x32\x10.gooseai.Request\x12$\n\ton_status\x18\x03 \x03(\x0b\x32\x11.gooseai.OnStatus\"A\n\x0c\x43hainRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1d\n\x05stage\x18\x02 \x03(\x0b\x32\x0e.gooseai.Stage*E\n\x0c\x46inishReason\x12\x08\n\x04NULL\x10\x00\x12\n\n\x06LENGTH\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\n\n\x06\x46ILTER\x10\x04*\xf8\x01\n\x0c\x41rtifactType\x12\x11\n\rARTIFACT_NONE\x10\x00\x12\x12\n\x0e\x41RTIFACT_IMAGE\x10\x01\x12\x12\n\x0e\x41RTIFACT_VIDEO\x10\x02\x12\x11\n\rARTIFACT_TEXT\x10\x03\x12\x13\n\x0f\x41RTIFACT_TOKENS\x10\x04\x12\x16\n\x12\x41RTIFACT_EMBEDDING\x10\x05\x12\x1c\n\x18\x41RTIFACT_CLASSIFICATIONS\x10\x06\x12\x11\n\rARTIFACT_MASK\x10\x07\x12\x13\n\x0f\x41RTIFACT_LATENT\x10\x08\x12\x13\n\x0f\x41RTIFACT_TENSOR\x10\t\x12\x12\n\x0e\x41RTIFACT_DEPTH\x10\n*g\n\x0eMaskedAreaInit\x12\x19\n\x15MASKED_AREA_INIT_ZERO\x10\x00\x12\x1b\n\x17MASKED_AREA_INIT_RANDOM\x10\x01\x12\x1d\n\x19MASKED_AREA_INIT_ORIGINAL\x10\x02*5\n\x0cWeightMethod\x12\x10\n\x0cTEXT_ENCODER\x10\x00\x12\x13\n\x0f\x43ROSS_ATTENTION\x10\x01*\x98\x02\n\x10\x44iffusionSampler\x12\x10\n\x0cSAMPLER_DDIM\x10\x00\x12\x10\n\x0cSAMPLER_DDPM\x10\x01\x12\x13\n\x0fSAMPLER_K_EULER\x10\x02\x12\x1d\n\x19SAMPLER_K_EULER_ANCESTRAL\x10\x03\x12\x12\n\x0eSAMPLER_K_HEUN\x10\x04\x12\x13\n\x0fSAMPLER_K_DPM_2\x10\x05\x12\x1d\n\x19SAMPLER_K_DPM_2_ANCESTRAL\x10\x06\x12\x11\n\rSAMPLER_K_LMS\x10\x07\x12 \n\x1cSAMPLER_K_DPMPP_2S_ANCESTRAL\x10\x08\x12\x16\n\x12SAMPLER_K_DPMPP_2M\x10\t\x12\x17\n\x13SAMPLER_K_DPMPP_SDE\x10\n*F\n\x08Upscaler\x12\x10\n\x0cUPSCALER_RGB\x10\x00\x12\x13\n\x0fUPSCALER_GFPGAN\x10\x01\x12\x13\n\x0fUPSCALER_ESRGAN\x10\x02*\xd8\x01\n\x0eGuidancePreset\x12\x18\n\x14GUIDANCE_PRESET_NONE\x10\x00\x12\x1a\n\x16GUIDANCE_PRESET_SIMPLE\x10\x01\x12\x1d\n\x19GUIDANCE_PRESET_FAST_BLUE\x10\x02\x12\x1e\n\x1aGUIDANCE_PRESET_FAST_GREEN\x10\x03\x12\x18\n\x14GUIDANCE_PRESET_SLOW\x10\x04\x12\x1a\n\x16GUIDANCE_PRESET_SLOWER\x10\x05\x12\x1b\n\x17GUIDANCE_PRESET_SLOWEST\x10\x06*\x91\x01\n\x11ModelArchitecture\x12\x1b\n\x17MODEL_ARCHITECTURE_NONE\x10\x00\x12\x1f\n\x1bMODEL_ARCHITECTURE_CLIP_VIT\x10\x01\x12\"\n\x1eMODEL_ARCHITECTURE_CLIP_RESNET\x10\x02\x12\x1a\n\x16MODEL_ARCHITECTURE_LDM\x10\x03*\xa2\x01\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_PASSTHROUGH\x10\x00\x12\x1f\n\x1b\x41\x43TION_REGENERATE_DUPLICATE\x10\x01\x12\x15\n\x11\x41\x43TION_REGENERATE\x10\x02\x12\x1e\n\x1a\x41\x43TION_OBFUSCATE_DUPLICATE\x10\x03\x12\x14\n\x10\x41\x43TION_OBFUSCATE\x10\x04\x12\x12\n\x0e\x41\x43TION_DISCARD\x10\x05*D\n\x0e\x43lassifierMode\x12\x17\n\x13\x43LSFR_MODE_ZEROSHOT\x10\x00\x12\x19\n\x15\x43LSFR_MODE_MULTICLASS\x10\x01*v\n\x0fInterpolateMode\x12\x16\n\x12INTERPOLATE_LINEAR\x10\x00\x12\x14\n\x10INTERPOLATE_RIFE\x10\x01\x12\x1a\n\x16INTERPOLATE_VAE_LINEAR\x10\x02\x12\x19\n\x15INTERPOLATE_VAE_SLERP\x10\x03*l\n\nBorderMode\x12\x12\n\x0e\x42ORDER_REFLECT\x10\x00\x12\x14\n\x10\x42ORDER_REPLICATE\x10\x01\x12\x0f\n\x0b\x42ORDER_WRAP\x10\x02\x12\x0f\n\x0b\x42ORDER_ZERO\x10\x03\x12\x12\n\x0e\x42ORDER_PREFILL\x10\x04*O\n\x0e\x43olorMatchMode\x12\x13\n\x0f\x43OLOR_MATCH_HSV\x10\x00\x12\x13\n\x0f\x43OLOR_MATCH_LAB\x10\x01\x12\x13\n\x0f\x43OLOR_MATCH_RGB\x10\x02*=\n\nCameraType\x12\x16\n\x12\x43\x41MERA_PERSPECTIVE\x10\x00\x12\x17\n\x13\x43\x41MERA_ORTHOGRAPHIC\x10\x01*=\n\x0b\x41ssetAction\x12\r\n\tASSET_PUT\x10\x00\x12\r\n\tASSET_GET\x10\x01\x12\x10\n\x0c\x41SSET_DELETE\x10\x02*\x81\x01\n\x08\x41ssetUse\x12\x17\n\x13\x41SSET_USE_UNDEFINED\x10\x00\x12\x13\n\x0f\x41SSET_USE_INPUT\x10\x01\x12\x14\n\x10\x41SSET_USE_OUTPUT\x10\x02\x12\x1a\n\x16\x41SSET_USE_INTERMEDIATE\x10\x03\x12\x15\n\x11\x41SSET_USE_PROJECT\x10\x04*W\n\x0bStageAction\x12\x15\n\x11STAGE_ACTION_PASS\x10\x00\x12\x18\n\x14STAGE_ACTION_DISCARD\x10\x01\x12\x17\n\x13STAGE_ACTION_RETURN\x10\x02\x32\x83\x01\n\x11GenerationService\x12\x31\n\x08Generate\x12\x10.gooseai.Request\x1a\x0f.gooseai.Answer\"\x00\x30\x01\x12;\n\rChainGenerate\x12\x15.gooseai.ChainRequest\x1a\x0f.gooseai.Answer\"\x00\x30\x01\x42;Z9github.com/stability-ai/api-interfaces/gooseai/generationb\x06proto3')

_FINISHREASON = DESCRIPTOR.enum_types_by_name['FinishReason']
FinishReason = enum_type_wrapper.EnumTypeWrapper(_FINISHREASON)
_ARTIFACTTYPE = DESCRIPTOR.enum_types_by_name['ArtifactType']
ArtifactType = enum_type_wrapper.EnumTypeWrapper(_ARTIFACTTYPE)
_MASKEDAREAINIT = DESCRIPTOR.enum_types_by_name['MaskedAreaInit']
MaskedAreaInit = enum_type_wrapper.EnumTypeWrapper(_MASKEDAREAINIT)
_WEIGHTMETHOD = DESCRIPTOR.enum_types_by_name['WeightMethod']
WeightMethod = enum_type_wrapper.EnumTypeWrapper(_WEIGHTMETHOD)
_DIFFUSIONSAMPLER = DESCRIPTOR.enum_types_by_name['DiffusionSampler']
DiffusionSampler = enum_type_wrapper.EnumTypeWrapper(_DIFFUSIONSAMPLER)
_UPSCALER = DESCRIPTOR.enum_types_by_name['Upscaler']
Upscaler = enum_type_wrapper.EnumTypeWrapper(_UPSCALER)
_GUIDANCEPRESET = DESCRIPTOR.enum_types_by_name['GuidancePreset']
GuidancePreset = enum_type_wrapper.EnumTypeWrapper(_GUIDANCEPRESET)
_MODELARCHITECTURE = DESCRIPTOR.enum_types_by_name['ModelArchitecture']
ModelArchitecture = enum_type_wrapper.EnumTypeWrapper(_MODELARCHITECTURE)
_ACTION = DESCRIPTOR.enum_types_by_name['Action']
Action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
_CLASSIFIERMODE = DESCRIPTOR.enum_types_by_name['ClassifierMode']
ClassifierMode = enum_type_wrapper.EnumTypeWrapper(_CLASSIFIERMODE)
_INTERPOLATEMODE = DESCRIPTOR.enum_types_by_name['InterpolateMode']
InterpolateMode = enum_type_wrapper.EnumTypeWrapper(_INTERPOLATEMODE)
_BORDERMODE = DESCRIPTOR.enum_types_by_name['BorderMode']
BorderMode = enum_type_wrapper.EnumTypeWrapper(_BORDERMODE)
_COLORMATCHMODE = DESCRIPTOR.enum_types_by_name['ColorMatchMode']
ColorMatchMode = enum_type_wrapper.EnumTypeWrapper(_COLORMATCHMODE)
_CAMERATYPE = DESCRIPTOR.enum_types_by_name['CameraType']
CameraType = enum_type_wrapper.EnumTypeWrapper(_CAMERATYPE)
_ASSETACTION = DESCRIPTOR.enum_types_by_name['AssetAction']
AssetAction = enum_type_wrapper.EnumTypeWrapper(_ASSETACTION)
_ASSETUSE = DESCRIPTOR.enum_types_by_name['AssetUse']
AssetUse = enum_type_wrapper.EnumTypeWrapper(_ASSETUSE)
_STAGEACTION = DESCRIPTOR.enum_types_by_name['StageAction']
StageAction = enum_type_wrapper.EnumTypeWrapper(_STAGEACTION)
NULL = 0
LENGTH = 1
STOP = 2
ERROR = 3
FILTER = 4
ARTIFACT_NONE = 0
ARTIFACT_IMAGE = 1
ARTIFACT_VIDEO = 2
ARTIFACT_TEXT = 3
ARTIFACT_TOKENS = 4
ARTIFACT_EMBEDDING = 5
ARTIFACT_CLASSIFICATIONS = 6
ARTIFACT_MASK = 7
ARTIFACT_LATENT = 8
ARTIFACT_TENSOR = 9
ARTIFACT_DEPTH = 10
MASKED_AREA_INIT_ZERO = 0
MASKED_AREA_INIT_RANDOM = 1
MASKED_AREA_INIT_ORIGINAL = 2
TEXT_ENCODER = 0
CROSS_ATTENTION = 1
SAMPLER_DDIM = 0
SAMPLER_DDPM = 1
SAMPLER_K_EULER = 2
SAMPLER_K_EULER_ANCESTRAL = 3
SAMPLER_K_HEUN = 4
SAMPLER_K_DPM_2 = 5
SAMPLER_K_DPM_2_ANCESTRAL = 6
SAMPLER_K_LMS = 7
SAMPLER_K_DPMPP_2S_ANCESTRAL = 8
SAMPLER_K_DPMPP_2M = 9
SAMPLER_K_DPMPP_SDE = 10
UPSCALER_RGB = 0
UPSCALER_GFPGAN = 1
UPSCALER_ESRGAN = 2
GUIDANCE_PRESET_NONE = 0
GUIDANCE_PRESET_SIMPLE = 1
GUIDANCE_PRESET_FAST_BLUE = 2
GUIDANCE_PRESET_FAST_GREEN = 3
GUIDANCE_PRESET_SLOW = 4
GUIDANCE_PRESET_SLOWER = 5
GUIDANCE_PRESET_SLOWEST = 6
MODEL_ARCHITECTURE_NONE = 0
MODEL_ARCHITECTURE_CLIP_VIT = 1
MODEL_ARCHITECTURE_CLIP_RESNET = 2
MODEL_ARCHITECTURE_LDM = 3
ACTION_PASSTHROUGH = 0
ACTION_REGENERATE_DUPLICATE = 1
ACTION_REGENERATE = 2
ACTION_OBFUSCATE_DUPLICATE = 3
ACTION_OBFUSCATE = 4
ACTION_DISCARD = 5
CLSFR_MODE_ZEROSHOT = 0
CLSFR_MODE_MULTICLASS = 1
INTERPOLATE_LINEAR = 0
INTERPOLATE_RIFE = 1
INTERPOLATE_VAE_LINEAR = 2
INTERPOLATE_VAE_SLERP = 3
BORDER_REFLECT = 0
BORDER_REPLICATE = 1
BORDER_WRAP = 2
BORDER_ZERO = 3
BORDER_PREFILL = 4
COLOR_MATCH_HSV = 0
COLOR_MATCH_LAB = 1
COLOR_MATCH_RGB = 2
CAMERA_PERSPECTIVE = 0
CAMERA_ORTHOGRAPHIC = 1
ASSET_PUT = 0
ASSET_GET = 1
ASSET_DELETE = 2
ASSET_USE_UNDEFINED = 0
ASSET_USE_INPUT = 1
ASSET_USE_OUTPUT = 2
ASSET_USE_INTERMEDIATE = 3
ASSET_USE_PROJECT = 4
STAGE_ACTION_PASS = 0
STAGE_ACTION_DISCARD = 1
STAGE_ACTION_RETURN = 2


_TOKEN = DESCRIPTOR.message_types_by_name['Token']
_TOKENS = DESCRIPTOR.message_types_by_name['Tokens']
_ARTIFACT = DESCRIPTOR.message_types_by_name['Artifact']
_PROMPTPARAMETERS = DESCRIPTOR.message_types_by_name['PromptParameters']
_PROMPT = DESCRIPTOR.message_types_by_name['Prompt']
_SAMPLERPARAMETERS = DESCRIPTOR.message_types_by_name['SamplerParameters']
_CONDITIONERPARAMETERS = DESCRIPTOR.message_types_by_name['ConditionerParameters']
_SCHEDULEPARAMETERS = DESCRIPTOR.message_types_by_name['ScheduleParameters']
_STEPPARAMETER = DESCRIPTOR.message_types_by_name['StepParameter']
_MODEL = DESCRIPTOR.message_types_by_name['Model']
_CUTOUTPARAMETERS = DESCRIPTOR.message_types_by_name['CutoutParameters']
_GUIDANCESCHEDULEPARAMETERS = DESCRIPTOR.message_types_by_name['GuidanceScheduleParameters']
_GUIDANCEINSTANCEPARAMETERS = DESCRIPTOR.message_types_by_name['GuidanceInstanceParameters']
_GUIDANCEPARAMETERS = DESCRIPTOR.message_types_by_name['GuidanceParameters']
_TRANSFORMTYPE = DESCRIPTOR.message_types_by_name['TransformType']
_IMAGEPARAMETERS = DESCRIPTOR.message_types_by_name['ImageParameters']
_CLASSIFIERCONCEPT = DESCRIPTOR.message_types_by_name['ClassifierConcept']
_CLASSIFIERCATEGORY = DESCRIPTOR.message_types_by_name['ClassifierCategory']
_CLASSIFIERPARAMETERS = DESCRIPTOR.message_types_by_name['ClassifierParameters']
_INTERPOLATEPARAMETERS = DESCRIPTOR.message_types_by_name['InterpolateParameters']
_TRANSFORMCOLORADJUST = DESCRIPTOR.message_types_by_name['TransformColorAdjust']
_TRANSFORMDEPTHCALC = DESCRIPTOR.message_types_by_name['TransformDepthCalc']
_TRANSFORMMATRIX = DESCRIPTOR.message_types_by_name['TransformMatrix']
_TRANSFORMRESAMPLE = DESCRIPTOR.message_types_by_name['TransformResample']
_POINTCLOUDRENDERPARAMETERS = DESCRIPTOR.message_types_by_name['PointCloudRenderParameters']
_MESHRENDERPARAMETERS = DESCRIPTOR.message_types_by_name['MeshRenderParameters']
_RENDERPARAMETERS = DESCRIPTOR.message_types_by_name['RenderParameters']
_CAMERAPARAMETERS = DESCRIPTOR.message_types_by_name['CameraParameters']
_TRANSFORMCAMERAPOSE = DESCRIPTOR.message_types_by_name['TransformCameraPose']
_TRANSFORMPARAMETERS = DESCRIPTOR.message_types_by_name['TransformParameters']
_ASSETPARAMETERS = DESCRIPTOR.message_types_by_name['AssetParameters']
_ANSWERMETA = DESCRIPTOR.message_types_by_name['AnswerMeta']
_ANSWER = DESCRIPTOR.message_types_by_name['Answer']
_ANSWERBATCH = DESCRIPTOR.message_types_by_name['AnswerBatch']
_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_ONSTATUS = DESCRIPTOR.message_types_by_name['OnStatus']
_STAGE = DESCRIPTOR.message_types_by_name['Stage']
_CHAINREQUEST = DESCRIPTOR.message_types_by_name['ChainRequest']
Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Token)
  })
_sym_db.RegisterMessage(Token)

Tokens = _reflection.GeneratedProtocolMessageType('Tokens', (_message.Message,), {
  'DESCRIPTOR' : _TOKENS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Tokens)
  })
_sym_db.RegisterMessage(Tokens)

Artifact = _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), {
  'DESCRIPTOR' : _ARTIFACT,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Artifact)
  })
_sym_db.RegisterMessage(Artifact)

PromptParameters = _reflection.GeneratedProtocolMessageType('PromptParameters', (_message.Message,), {
  'DESCRIPTOR' : _PROMPTPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.PromptParameters)
  })
_sym_db.RegisterMessage(PromptParameters)

Prompt = _reflection.GeneratedProtocolMessageType('Prompt', (_message.Message,), {
  'DESCRIPTOR' : _PROMPT,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Prompt)
  })
_sym_db.RegisterMessage(Prompt)

SamplerParameters = _reflection.GeneratedProtocolMessageType('SamplerParameters', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLERPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.SamplerParameters)
  })
_sym_db.RegisterMessage(SamplerParameters)

ConditionerParameters = _reflection.GeneratedProtocolMessageType('ConditionerParameters', (_message.Message,), {
  'DESCRIPTOR' : _CONDITIONERPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ConditionerParameters)
  })
_sym_db.RegisterMessage(ConditionerParameters)

ScheduleParameters = _reflection.GeneratedProtocolMessageType('ScheduleParameters', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ScheduleParameters)
  })
_sym_db.RegisterMessage(ScheduleParameters)

StepParameter = _reflection.GeneratedProtocolMessageType('StepParameter', (_message.Message,), {
  'DESCRIPTOR' : _STEPPARAMETER,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.StepParameter)
  })
_sym_db.RegisterMessage(StepParameter)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Model)
  })
_sym_db.RegisterMessage(Model)

CutoutParameters = _reflection.GeneratedProtocolMessageType('CutoutParameters', (_message.Message,), {
  'DESCRIPTOR' : _CUTOUTPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CutoutParameters)
  })
_sym_db.RegisterMessage(CutoutParameters)

GuidanceScheduleParameters = _reflection.GeneratedProtocolMessageType('GuidanceScheduleParameters', (_message.Message,), {
  'DESCRIPTOR' : _GUIDANCESCHEDULEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GuidanceScheduleParameters)
  })
_sym_db.RegisterMessage(GuidanceScheduleParameters)

GuidanceInstanceParameters = _reflection.GeneratedProtocolMessageType('GuidanceInstanceParameters', (_message.Message,), {
  'DESCRIPTOR' : _GUIDANCEINSTANCEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GuidanceInstanceParameters)
  })
_sym_db.RegisterMessage(GuidanceInstanceParameters)

GuidanceParameters = _reflection.GeneratedProtocolMessageType('GuidanceParameters', (_message.Message,), {
  'DESCRIPTOR' : _GUIDANCEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.GuidanceParameters)
  })
_sym_db.RegisterMessage(GuidanceParameters)

TransformType = _reflection.GeneratedProtocolMessageType('TransformType', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMTYPE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformType)
  })
_sym_db.RegisterMessage(TransformType)

ImageParameters = _reflection.GeneratedProtocolMessageType('ImageParameters', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ImageParameters)
  })
_sym_db.RegisterMessage(ImageParameters)

ClassifierConcept = _reflection.GeneratedProtocolMessageType('ClassifierConcept', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERCONCEPT,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ClassifierConcept)
  })
_sym_db.RegisterMessage(ClassifierConcept)

ClassifierCategory = _reflection.GeneratedProtocolMessageType('ClassifierCategory', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERCATEGORY,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ClassifierCategory)
  })
_sym_db.RegisterMessage(ClassifierCategory)

ClassifierParameters = _reflection.GeneratedProtocolMessageType('ClassifierParameters', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ClassifierParameters)
  })
_sym_db.RegisterMessage(ClassifierParameters)

InterpolateParameters = _reflection.GeneratedProtocolMessageType('InterpolateParameters', (_message.Message,), {
  'DESCRIPTOR' : _INTERPOLATEPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.InterpolateParameters)
  })
_sym_db.RegisterMessage(InterpolateParameters)

TransformColorAdjust = _reflection.GeneratedProtocolMessageType('TransformColorAdjust', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMCOLORADJUST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformColorAdjust)
  })
_sym_db.RegisterMessage(TransformColorAdjust)

TransformDepthCalc = _reflection.GeneratedProtocolMessageType('TransformDepthCalc', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMDEPTHCALC,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformDepthCalc)
  })
_sym_db.RegisterMessage(TransformDepthCalc)

TransformMatrix = _reflection.GeneratedProtocolMessageType('TransformMatrix', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMMATRIX,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformMatrix)
  })
_sym_db.RegisterMessage(TransformMatrix)

TransformResample = _reflection.GeneratedProtocolMessageType('TransformResample', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMRESAMPLE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformResample)
  })
_sym_db.RegisterMessage(TransformResample)

PointCloudRenderParameters = _reflection.GeneratedProtocolMessageType('PointCloudRenderParameters', (_message.Message,), {
  'DESCRIPTOR' : _POINTCLOUDRENDERPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.PointCloudRenderParameters)
  })
_sym_db.RegisterMessage(PointCloudRenderParameters)

MeshRenderParameters = _reflection.GeneratedProtocolMessageType('MeshRenderParameters', (_message.Message,), {
  'DESCRIPTOR' : _MESHRENDERPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.MeshRenderParameters)
  })
_sym_db.RegisterMessage(MeshRenderParameters)

RenderParameters = _reflection.GeneratedProtocolMessageType('RenderParameters', (_message.Message,), {
  'DESCRIPTOR' : _RENDERPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.RenderParameters)
  })
_sym_db.RegisterMessage(RenderParameters)

CameraParameters = _reflection.GeneratedProtocolMessageType('CameraParameters', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.CameraParameters)
  })
_sym_db.RegisterMessage(CameraParameters)

TransformCameraPose = _reflection.GeneratedProtocolMessageType('TransformCameraPose', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMCAMERAPOSE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformCameraPose)
  })
_sym_db.RegisterMessage(TransformCameraPose)

TransformParameters = _reflection.GeneratedProtocolMessageType('TransformParameters', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.TransformParameters)
  })
_sym_db.RegisterMessage(TransformParameters)

AssetParameters = _reflection.GeneratedProtocolMessageType('AssetParameters', (_message.Message,), {
  'DESCRIPTOR' : _ASSETPARAMETERS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.AssetParameters)
  })
_sym_db.RegisterMessage(AssetParameters)

AnswerMeta = _reflection.GeneratedProtocolMessageType('AnswerMeta', (_message.Message,), {
  'DESCRIPTOR' : _ANSWERMETA,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.AnswerMeta)
  })
_sym_db.RegisterMessage(AnswerMeta)

Answer = _reflection.GeneratedProtocolMessageType('Answer', (_message.Message,), {
  'DESCRIPTOR' : _ANSWER,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Answer)
  })
_sym_db.RegisterMessage(Answer)

AnswerBatch = _reflection.GeneratedProtocolMessageType('AnswerBatch', (_message.Message,), {
  'DESCRIPTOR' : _ANSWERBATCH,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.AnswerBatch)
  })
_sym_db.RegisterMessage(AnswerBatch)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Request)
  })
_sym_db.RegisterMessage(Request)

OnStatus = _reflection.GeneratedProtocolMessageType('OnStatus', (_message.Message,), {
  'DESCRIPTOR' : _ONSTATUS,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.OnStatus)
  })
_sym_db.RegisterMessage(OnStatus)

Stage = _reflection.GeneratedProtocolMessageType('Stage', (_message.Message,), {
  'DESCRIPTOR' : _STAGE,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Stage)
  })
_sym_db.RegisterMessage(Stage)

ChainRequest = _reflection.GeneratedProtocolMessageType('ChainRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHAINREQUEST,
  '__module__' : 'generation_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ChainRequest)
  })
_sym_db.RegisterMessage(ChainRequest)

_GENERATIONSERVICE = DESCRIPTOR.services_by_name['GenerationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z9github.com/stability-ai/api-interfaces/gooseai/generation'
  _TRANSFORMMATRIX.fields_by_name['data']._options = None
  _TRANSFORMMATRIX.fields_by_name['data']._serialized_options = b'\020\001'
  _FINISHREASON._serialized_start=6755
  _FINISHREASON._serialized_end=6824
  _ARTIFACTTYPE._serialized_start=6827
  _ARTIFACTTYPE._serialized_end=7075
  _MASKEDAREAINIT._serialized_start=7077
  _MASKEDAREAINIT._serialized_end=7180
  _WEIGHTMETHOD._serialized_start=7182
  _WEIGHTMETHOD._serialized_end=7235
  _DIFFUSIONSAMPLER._serialized_start=7238
  _DIFFUSIONSAMPLER._serialized_end=7518
  _UPSCALER._serialized_start=7520
  _UPSCALER._serialized_end=7590
  _GUIDANCEPRESET._serialized_start=7593
  _GUIDANCEPRESET._serialized_end=7809
  _MODELARCHITECTURE._serialized_start=7812
  _MODELARCHITECTURE._serialized_end=7957
  _ACTION._serialized_start=7960
  _ACTION._serialized_end=8122
  _CLASSIFIERMODE._serialized_start=8124
  _CLASSIFIERMODE._serialized_end=8192
  _INTERPOLATEMODE._serialized_start=8194
  _INTERPOLATEMODE._serialized_end=8312
  _BORDERMODE._serialized_start=8314
  _BORDERMODE._serialized_end=8422
  _COLORMATCHMODE._serialized_start=8424
  _COLORMATCHMODE._serialized_end=8503
  _CAMERATYPE._serialized_start=8505
  _CAMERATYPE._serialized_end=8566
  _ASSETACTION._serialized_start=8568
  _ASSETACTION._serialized_end=8629
  _ASSETUSE._serialized_start=8632
  _ASSETUSE._serialized_end=8761
  _STAGEACTION._serialized_start=8763
  _STAGEACTION._serialized_end=8850
  _TOKEN._serialized_start=74
  _TOKEN._serialized_end=121
  _TOKENS._serialized_start=123
  _TOKENS._serialized_end=207
  _ARTIFACT._serialized_start=210
  _ARTIFACT._serialized_end=581
  _PROMPTPARAMETERS._serialized_start=583
  _PROMPTPARAMETERS._serialized_end=661
  _PROMPT._serialized_start=664
  _PROMPT._serialized_end=839
  _SAMPLERPARAMETERS._serialized_start=842
  _SAMPLERPARAMETERS._serialized_end=1185
  _CONDITIONERPARAMETERS._serialized_start=1188
  _CONDITIONERPARAMETERS._serialized_end=1327
  _SCHEDULEPARAMETERS._serialized_start=1329
  _SCHEDULEPARAMETERS._serialized_end=1435
  _STEPPARAMETER._serialized_start=1438
  _STEPPARAMETER._serialized_end=1666
  _MODEL._serialized_start=1669
  _MODEL._serialized_end=1820
  _CUTOUTPARAMETERS._serialized_start=1823
  _CUTOUTPARAMETERS._serialized_end=2011
  _GUIDANCESCHEDULEPARAMETERS._serialized_start=2013
  _GUIDANCESCHEDULEPARAMETERS._serialized_end=2074
  _GUIDANCEINSTANCEPARAMETERS._serialized_start=2077
  _GUIDANCEINSTANCEPARAMETERS._serialized_end=2356
  _GUIDANCEPARAMETERS._serialized_start=2358
  _GUIDANCEPARAMETERS._serialized_end=2484
  _TRANSFORMTYPE._serialized_start=2486
  _TRANSFORMTYPE._serialized_end=2596
  _IMAGEPARAMETERS._serialized_start=2599
  _IMAGEPARAMETERS._serialized_end=3044
  _CLASSIFIERCONCEPT._serialized_start=3046
  _CLASSIFIERCONCEPT._serialized_end=3120
  _CLASSIFIERCATEGORY._serialized_start=3123
  _CLASSIFIERCATEGORY._serialized_end=3367
  _CLASSIFIERPARAMETERS._serialized_start=3370
  _CLASSIFIERPARAMETERS._serialized_end=3554
  _INTERPOLATEPARAMETERS._serialized_start=3556
  _INTERPOLATEPARAMETERS._serialized_end=3649
  _TRANSFORMCOLORADJUST._serialized_start=3652
  _TRANSFORMCOLORADJUST._serialized_end=4064
  _TRANSFORMDEPTHCALC._serialized_start=4067
  _TRANSFORMDEPTHCALC._serialized_end=4207
  _TRANSFORMMATRIX._serialized_start=4209
  _TRANSFORMMATRIX._serialized_end=4244
  _TRANSFORMRESAMPLE._serialized_start=4247
  _TRANSFORMRESAMPLE._serialized_end=4509
  _POINTCLOUDRENDERPARAMETERS._serialized_start=4511
  _POINTCLOUDRENDERPARAMETERS._serialized_end=4581
  _MESHRENDERPARAMETERS._serialized_start=4583
  _MESHRENDERPARAMETERS._serialized_end=4628
  _RENDERPARAMETERS._serialized_start=4631
  _RENDERPARAMETERS._serialized_end=4798
  _CAMERAPARAMETERS._serialized_start=4800
  _CAMERAPARAMETERS._serialized_end=4925
  _TRANSFORMCAMERAPOSE._serialized_start=4928
  _TRANSFORMCAMERAPOSE._serialized_end=5198
  _TRANSFORMPARAMETERS._serialized_start=5201
  _TRANSFORMPARAMETERS._serialized_end=5442
  _ASSETPARAMETERS._serialized_start=5444
  _ASSETPARAMETERS._serialized_end=5551
  _ANSWERMETA._serialized_start=5554
  _ANSWERMETA._serialized_end=5702
  _ANSWER._serialized_start=5705
  _ANSWER._serialized_end=5874
  _ANSWERBATCH._serialized_start=5876
  _ANSWERBATCH._serialized_end=5941
  _REQUEST._serialized_start=5944
  _REQUEST._serialized_end=6471
  _ONSTATUS._serialized_start=6473
  _ONSTATUS._serialized_end=6592
  _STAGE._serialized_start=6594
  _STAGE._serialized_end=6686
  _CHAINREQUEST._serialized_start=6688
  _CHAINREQUEST._serialized_end=6753
  _GENERATIONSERVICE._serialized_start=8853
  _GENERATIONSERVICE._serialized_end=8984
# @@protoc_insertion_point(module_scope)
