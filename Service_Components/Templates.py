# -*- coding: utf-8 -*-

#### Schemas
source_cr_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "common_part": {
      "type": "object",
      "properties": {
        "version": {
          "type": "string"
        },
        "cr_id": {
          "type": "string"
        },
        "surrogate_id": {
          "type": "string"
        },
        "rs_description": {
          "type": "object",
          "properties": {
            "resource_set": {
              "type": "object",
              "properties": {
                "rs_id": {
                  "type": "string"
                },
                "dataset": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "dataset_id": {
                        "type": "string"
                      },
                      "distribution_id": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "dataset_id",
                      "distribution_id"
                    ]
                  }
                }
              },
              "required": [
                "rs_id",
                "dataset"
              ]
            }
          },
          "required": [
            "resource_set"
          ]
        },
        "slr_id": {
          "type": "string"
        },
        "iat": {
          "type": "integer"
        },
        "nbf": {
          "type": "integer"
        },
        "exp": {
          "type": "integer"
        },
        "operator": {
          "type": "string"
        },
        "subject_id": {
          "type": "string"
        },
        "role": {
          "type": "string"
        }
      },
      "required": [
        "version",
        "cr_id",
        "surrogate_id",
        "rs_description",
        "slr_id",
        "iat",
        "nbf",
        "exp",
        "operator",
        "subject_id",
        "role"
      ]
    },
    "role_specific_part": {
      "type": "object",
      "properties": {
        "auth_token_issuer_key": {
          "type": "object",
          "properties": {}
        }
      },
      "required": [
        "token_issuer_key"
      ]
    },
    "consent_receipt_part": {
      "type": "object",
      "properties": {
        "ki_cr": {
          "type": "object",
          "properties": {}
        }
      },
      "required": [
        "ki_cr"
      ]
    },
    "extension_part": {
      "type": "object",
      "properties": {
        "extensions": {
          "type": "object",
          "properties": {}
        }
      },
      "required": [
        "extensions"
      ]
    }
  },
  "required": [
    "common_part",
    "role_specific_part",
    "consent_receipt_part",
    "extension_part"
  ]
}

sink_cr_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "common_part": {
      "type": "object",
      "properties": {
        "version": {
          "type": "string"
        },
        "cr_id": {
          "type": "string"
        },
        "surrogate_id": {
          "type": "string"
        },
        "rs_description": {
          "type": "object",
          "properties": {
            "resource_set": {
              "type": "object",
              "properties": {
                "rs_id": {
                  "type": "string"
                },
                "dataset": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "dataset_id": {
                        "type": "string"
                      },
                      "distribution_id": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "dataset_id",
                      "distribution_id"
                    ]
                  }
                }
              },
              "required": [
                "rs_id",
                "dataset"
              ]
            }
          },
          "required": [
            "resource_set"
          ]
        },
        "slr_id": {
          "type": "string"
        },
        "iat": {
          "type": "integer"
        },
        "nbf": {
          "type": "integer"
        },
        "exp": {
          "type": "integer"
        },
        "operator": {
          "type": "string"
        },
        "subject_id": {
          "type": "string"
        },
        "role": {
          "type": "string"
        }
      },
      "required": [
        "version",
        "cr_id",
        "surrogate_id",
        "rs_description",
        "slr_id",
        "iat",
        "nbf",
        "exp",
        "operator",
        "subject_id",
        "role"
      ]
    },
    "role_specific_part": {
      "type": "object",
      "properties": {
        "usage_rules": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "source_cr_id": {
          "type": "string"
        }
      },
      "required": [
        "usage_rules",
        "source_cr_id"
      ]
    },
    "consent_receipt_part": {
      "type": "object",
      "properties": {
        "ki_cr": {
          "type": "object",
          "properties": {}
        }
      },
      "required": [
        "ki_cr"
      ]
    },
    "extension_part": {
      "type": "object",
      "properties": {
        "extensions": {
          "type": "object",
          "properties": {}
        }
      },
      "required": [
        "extensions"
      ]
    }
  },
  "required": [
    "common_part",
    "role_specific_part",
    "consent_receipt_part",
    "extension_part"
  ]
}

csr_schema = {
  "iat": 1471857663,
  "prev_record_id": "null",
  "cr_id": "833dbc2b-bb11-425c-9c66-42b4c104f8da",
  "account_id": "48e2a067-c268-4bcb-b069-68c16bf45c5b_2",
  "record_id": "f8f01397-d5e7-4e5d-ac48-c42707a4f0b8",
  "consent_status": "Active"
}
