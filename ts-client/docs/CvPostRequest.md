
# CvPostRequest


## Properties

Name | Type
------------ | -------------
`firstName` | string
`lastName` | string

## Example

```typescript
import type { CvPostRequest } from '@dubhar/cv-client'

// TODO: Update the object below with actual values
const example = {
  "firstName": John,
  "lastName": Doe,
} satisfies CvPostRequest

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CvPostRequest
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


