# Backend Task 2 (Simple Arithmetic)
This is an application performs  a simple arithmetic on the payload to a `POST` [Endpoint](https://ml-app-idris01.koyeb.app/) that returns a simple (`JSON`) with the result

Usage:

Send post request to `https://ml-app-idris01.koyeb.app/` of the following form

e.g 
```curl -X POST -H "Accept:application/json" \
	-d '{"operation_type":"subtraction","x":5,\
	"y":8}' https://ml-app-idris01.koyeb.app/
```

Response (json):

```
{
	"slackUsername":"Idris Adebowale",
	"result":3,
	"operation_type":"subtraction"
}
```
