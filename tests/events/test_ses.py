import aws_lambda_typing as lambda_typing


def test_ses_event() -> None:
    dummy: lambda_typing.SESEvent = {
        "Records": [
            {
                "eventVersion": "1.0",
                "ses": {
                    "mail": {
                        "commonHeaders": {
                            "from": [
                                "Jane Doe <janedoe@example.com>"
                            ],
                            "to": [
                                "johndoe@example.com"
                            ],
                            "returnPath": "janedoe@example.com",
                            "messageId": "<0123456789example.com>",
                            "date": "Wed, 7 Oct 2015 12:34:56 -0700",
                            "subject": "Test Subject"
                        },
                        "source": "janedoe@example.com",
                        "timestamp": "1970-01-01T00:00:00.000Z",
                        "destination": [
                            "johndoe@example.com"
                        ],
                        "headers": [
                            {
                                "name": "Return-Path",
                                "value": "<janedoe@example.com>"
                            },
                            {
                                "name": "Received",
                                "value": "from mailer.example.com (mailer.example.com [203.0.113.1]) by inbound-smtp.us-west-2.amazonaws.com with SMTP id o3vrnil0e2ic for johndoe@example.com; Wed, 07 Oct 2015 12:34:56 +0000 (UTC)"
                            },
                            {
                                "name": "DKIM-Signature",
                                "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=example.com; s=example; h=mime-version:from:date:message-id:subject:to:content-type; bh=jX3F0bCAI7sIbkHyy3mLYO28ieDQz2R0P8HwQkklFj4=; b=sQwJ+LMe9RjkesGu+vqU56asvMhrLRRYrWCbV"
                            },
                            {
                                "name": "MIME-Version",
                                "value": "1.0"
                            },
                            {
                                "name": "From",
                                "value": "Jane Doe <janedoe@example.com>"
                            },
                            {
                                "name": "Date",
                                "value": "Wed, 7 Oct 2015 12:34:56 -0700"
                            },
                            {
                                "name": "Message-ID",
                                "value": "<0123456789example.com>"
                            },
                            {
                                "name": "Subject",
                                "value": "Test Subject"
                            },
                            {
                                "name": "To",
                                "value": "johndoe@example.com"
                            },
                            {
                                "name": "Content-Type",
                                "value": "text/plain; charset=UTF-8"
                            }
                        ],
                        "headersTruncated": False,
                        "messageId": "o3vrnil0e2ic28tr"
                    },
                    "receipt": {
                        "recipients": [
                            "johndoe@example.com"
                        ],
                        "timestamp": "1970-01-01T00:00:00.000Z",
                        "spamVerdict": {
                            "status": "PASS"
                        },
                        "dkimVerdict": {
                            "status": "PASS"
                        },
                        "processingTimeMillis": 574,
                        "action": {
                            "type": "Lambda",
                            "invocationType": "Event",
                            "functionArn": "arn:aws:lambda:us-west-2:012345678912:function:Example"
                        },
                        "spfVerdict": {
                            "status": "PASS"
                        },
                        "virusVerdict": {
                            "status": "PASS"
                        }
                    }
                },
                "eventSource": "aws:ses"
            }
        ]
    }
