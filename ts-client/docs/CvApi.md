# CvApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cvPost**](CvApi.md#cvpostoperation) | **POST** /cv | Download CV PDF |



## cvPost

> Blob cvPost(cvPostRequest)

Download CV PDF

Returns the CV of the person matching the given first and last name as a PDF file.

### Example

```ts
import {
  Configuration,
  CvApi,
} from '@dubhar/cv-client';
import type { CvPostOperationRequest } from '@dubhar/cv-client';

async function example() {
  console.log("🚀 Testing @dubhar/cv-client SDK...");
  const api = new CvApi();

  const body = {
    // CvPostRequest
    cvPostRequest: ...,
  } satisfies CvPostOperationRequest;

  try {
    const data = await api.cvPost(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **cvPostRequest** | [CvPostRequest](CvPostRequest.md) |  | |

### Return type

**Blob**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/pdf`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CV PDF file |  -  |
| **404** | CV not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

