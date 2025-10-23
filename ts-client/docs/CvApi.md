# CvApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cvGet**](CvApi.md#cvget) | **GET** /cv | Download CV PDF |



## cvGet

> Blob cvGet(firstName, lastName)

Download CV PDF

Returns the CV of the person matching the given first and last name as a PDF file.

### Example

```ts
import {
  Configuration,
  CvApi,
} from '@dubhar/cv-client';
import type { CvGetRequest } from '@dubhar/cv-client';

async function example() {
  console.log("🚀 Testing @dubhar/cv-client SDK...");
  const api = new CvApi();

  const body = {
    // string | Person\'s first name
    firstName: firstName_example,
    // string | Person\'s last name
    lastName: lastName_example,
  } satisfies CvGetRequest;

  try {
    const data = await api.cvGet(body);
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
| **firstName** | `string` | Person\&#39;s first name | [Defaults to `undefined`] |
| **lastName** | `string` | Person\&#39;s last name | [Defaults to `undefined`] |

### Return type

**Blob**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/pdf`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CV PDF file |  -  |
| **404** | CV not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

