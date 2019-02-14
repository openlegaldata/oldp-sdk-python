# CourtMinimal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Full name of the court with location | 
**slug** | **str** | Type &amp; city name as lowercase | 
**city** | **int** | Court belongs to this city, if null court is state-level | [optional] 
**state** | **int** | Court belongs to this state (derive country of this field) | 
**jurisdiction** | **str** | Jurisdiction of court (ordinary, civil, ...) | [optional] 
**level_of_appeal** | **str** | Subject-matter jurisdiction (local, federal, high court, ...) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


