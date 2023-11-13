from flasgger import swag_from

template = {
    "swagger": "2.0",
    "info": {
        "title": "ML Validation Service API Documentation",
        "description": "API documentation for the Aerotract ML Validation tool",
        "version": "1.0.0"
    }
}

swag_mlval = swag_from({
    'responses': {
        200: {
                "description": "Successfully submitted operation",
                "schema": {
                    "type": "object",
                    "properties": {
                        "metrics": {
                            "type": "string",
                            "description": "Various ML metrics"
                        }
                    }
                }
            },
        500: {
            'description': 'Failed to submit operation',
            'schema': {
                'type': 'string',
            }
        }
    },
    'parameters': [
        {
            'name': 'client_id',
            'description': 'Client ID of data to process',
            'example': '10007',
            'in': 'body',
            'required': True,
            'type': 'string'
        },{
            'name': 'project_id',
            'description': 'Project ID of data to process',
            'example': '101036',
            'in': 'body',
            'required': True,
            'type': 'string'
        },{
            'name': 'stand_id',
            'description': 'Stand ID of data to process',
            'example': '103',
            'in': 'body',
            'required': True,
            'type': 'string'
        }
    ]
})