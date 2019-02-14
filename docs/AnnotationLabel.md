# AnnotationLabel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**owner** | **str** |  | [optional] 
**trusted** | **str** |  | [optional] 
**name** | **str** | Verbose name, e.g. This Awesome annotation | 
**slug** | **str** | Identifier, e.g. this-awesome-annotation | 
**private** | **bool** | Private annotations are only visible to its author | [optional] 
**many_annotations_per_label** | **bool** | A content object can have more than one annotation per label | [optional] 
**use_marker** | **bool** | Marker annotations are extracted from the text content and have a position in the text | [optional] 
**annotation_value_type** | **str** | Annotation values must be in this data type | [optional] 
**color** | **str** |  | [optional] 
**created_at** | **datetime** | Entry is created at this date time | [optional] 
**updated_at** | **datetime** | Date time of last change | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


