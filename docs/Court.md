# Court

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Full name of the court with location | 
**court_type** | **str** | Court type AG,VG,... | [optional] 
**city** | **int** | Court belongs to this city, if null court is state-level | [optional] 
**state** | **int** | Court belongs to this state (derive country of this field) | 
**code** | **str** | Unique court identifier based on ECLI (e.g. BVerfG) | 
**slug** | **str** | Type &amp; city name as lowercase | 
**description** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**homepage** | **str** | Official court homepage | [optional] 
**street_address** | **str** | Street address with house number | [optional] 
**postal_code** | **str** | Postal code (ZIP code) | [optional] 
**address_locality** | **str** | Locality (city name) | [optional] 
**telephone** | **str** | Telephone number | [optional] 
**fax_number** | **str** | Fax number | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


