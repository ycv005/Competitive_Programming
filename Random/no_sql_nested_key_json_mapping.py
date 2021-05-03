def get_separator():
    return "."


def formatted_type(a):
    return str(type(a)).split("'")[1]


def create_nested_key_dictionary_mapping(dic):
    res = []
    if dic and isinstance(dic, dict):
        for k, v in dic.items():
            if isinstance(v, dict):
                tmp = create_nested_key_dictionary_mapping(v)
                tmp = [str(k) + get_separator() + s for s in tmp]
                res += tmp
            elif isinstance(v, list):
                tmp = "0"
            else:
                tmp = str(k) + get_separator() + formatted_type(v)
                res.append(tmp)
    return res


d = {
    "shipment_id": "16195259718381635633J",
    "affiliate_details": {
        "id": "5ea6821b3425bb07c82a25c1",
        "affiliate_bag_id": None,
        "affiliate_order_id": "16195257569000112W",
        "company_affiliate_tag": None,
        "affiliate_id": "5ea6821b3425bb07c82a25c1",
        "affiliate_shipment_id": "16195259718381635633J",
        "shipment_meta": {
            "dp_id": 1,
            "weight": 0.2,
            "dimension": {
                "width": 1,
                "height": 1,
                "length": 111,
                "width_unit": "CM",
                "height_unit": "CM",
                "length_unit": "CM"
            },
            "timestamp": {
                "max": 1620476139,
                "min": 1620130539
            },
            "mixed_cart": False,
            "weight_unit": "KG",
            "ewaybill_info": None,
            "logistics_meta": {
                "dp_sort_key": "fm_priority",
                "account_info": {
                    "area_code": None,
                    "operations": "inter_city",
                    "fm_priority": 1,
                    "lm_priority": 1,
                    "payment_mode": "all",
                    "rvp_priority": 1,
                    "transport_mode": "air",
                    "assign_dp_from_sb": True,
                    "external_account_id": None,
                    "internal_account_id": "1"
                },
                "account_options": [
                    {
                        "area_code": None,
                        "operations": "inter_city",
                        "fm_priority": 1,
                        "lm_priority": 1,
                        "payment_mode": "all",
                        "rvp_priority": 1,
                        "transport_mode": "air",
                        "assign_dp_from_sb": True,
                        "external_account_id": None,
                        "internal_account_id": "1"
                    }
                ],
                "assign_dp_from_sb": True
            },
            "store_invoice_updated_date": "2021-04-27T17:46:44+00:00"
        },
        "affiliate_meta": {
            "fynd": {
                "fulfilment_identifier": "infibeam"
            }
        },
        "affiliate_store_id": None,
        "pdf_links": {},
        "config": {}
    },
    "app_id": "5ea6821b3425bb07c82a25c1",
    "article_details": {
        "status": {
            "return_accepted": {
                "rvsqskqcnm": {
                    "uid": "rvsqskqcnm",
                    "_id": "",
                    "is_set": "",
                    "bag_ids": [
                        11250
                    ],
                    "quantity": 1,
                    "reasons": {
                        "4": [
                            {
                                "slug": "card_issues",
                                "display_name": "Card issues",
                                "id": 4,
                                "state": "accept_buy_request",
                                "text": None,
                                "bag_id": 11250
                            }
                        ]
                    }
                }
            }
        }
    },
    "bag_status_history": [
        {
            "bag_id": 11250,
            "id": 31567,
            "delivery_partner_id": None,
            "status": "pending",
            "delivery_awb_number": None,
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:45:58+00:00",
            "created_at": "2021-04-27T17:45:58+00:00",
            "state_id": 89,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Pending",
                "app_facing": True,
                "is_active": True,
                "id": 89,
                "notify_customer": True,
                "journey_type": "forward",
                "app_display_name": "Pending",
                "app_state_name": "pending",
                "state_type": "operational",
                "name": "pending"
            }
        },
        {
            "bag_id": 11250,
            "id": 31568,
            "delivery_partner_id": None,
            "status": "placed",
            "delivery_awb_number": None,
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:45:58+00:00",
            "created_at": "2021-04-27T17:45:58+00:00",
            "state_id": 1,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Placed",
                "app_facing": True,
                "is_active": True,
                "id": 1,
                "notify_customer": True,
                "journey_type": "forward",
                "app_display_name": "Ordered",
                "app_state_name": "processing",
                "state_type": "operational",
                "name": "placed"
            }
        },
        {
            "bag_id": 11250,
            "id": 31569,
            "delivery_partner_id": None,
            "status": "bag_confirmed",
            "delivery_awb_number": None,
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:46:38+00:00",
            "created_at": "2021-04-27T17:46:38+00:00",
            "state_id": 2,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Bag Confirmed",
                "app_facing": True,
                "is_active": True,
                "id": 2,
                "notify_customer": False,
                "journey_type": "forward",
                "app_display_name": "Ordered",
                "app_state_name": "confirmed",
                "state_type": "operational",
                "name": "bag_confirmed"
            }
        },
        {
            "bag_id": 11250,
            "id": 31570,
            "delivery_partner_id": None,
            "status": "bag_invoiced",
            "delivery_awb_number": None,
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:46:44+00:00",
            "created_at": "2021-04-27T17:46:44+00:00",
            "state_id": 91,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Under Process",
                "app_facing": True,
                "is_active": True,
                "id": 91,
                "notify_customer": False,
                "journey_type": "forward",
                "app_display_name": "Under Process",
                "app_state_name": "bag_invoiced",
                "state_type": "operational",
                "name": "bag_invoiced"
            }
        },
        {
            "bag_id": 11250,
            "id": 31571,
            "delivery_partner_id": None,
            "status": "bag_packed",
            "delivery_awb_number": None,
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:47:10+00:00",
            "created_at": "2021-04-27T17:47:10+00:00",
            "state_id": 8,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Bag Packed",
                "app_facing": True,
                "is_active": True,
                "id": 8,
                "notify_customer": True,
                "journey_type": "forward",
                "app_display_name": "Under Process",
                "app_state_name": "bag_packed",
                "state_type": "operational",
                "name": "bag_packed"
            }
        },
        {
            "bag_id": 11250,
            "id": 31572,
            "delivery_partner_id": 1,
            "status": "dp_assigned",
            "delivery_awb_number": "711059984",
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:47:11+00:00",
            "created_at": "2021-04-27T17:47:11+00:00",
            "state_id": 7,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "DP Assigned",
                "app_facing": False,
                "is_active": True,
                "id": 7,
                "notify_customer": False,
                "journey_type": "forward",
                "app_display_name": "DP Assigned",
                "app_state_name": "dp_assigned",
                "state_type": "operational",
                "name": "dp_assigned"
            }
        },
        {
            "bag_id": 11250,
            "id": 31573,
            "delivery_partner_id": 1,
            "status": "handed_over_to_dg",
            "delivery_awb_number": "711059984",
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:47:20+00:00",
            "created_at": "2021-04-27T17:47:20+00:00",
            "state_id": 10,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Handed Over to DG",
                "app_facing": True,
                "is_active": True,
                "id": 10,
                "notify_customer": True,
                "journey_type": "forward",
                "app_display_name": "Under Process",
                "app_state_name": "bag_packed",
                "state_type": "operational",
                "name": "handed_over_to_dg"
            }
        },
        {
            "bag_id": 11250,
            "id": 31574,
            "delivery_partner_id": 1,
            "status": "bag_picked",
            "delivery_awb_number": "711059984",
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:47:33+00:00",
            "created_at": "2021-04-27T17:47:33+00:00",
            "state_id": 12,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "In Transit",
                "app_facing": True,
                "is_active": True,
                "id": 12,
                "notify_customer": False,
                "journey_type": "forward",
                "app_display_name": "Shipped",
                "app_state_name": "in_transit",
                "state_type": "operational",
                "name": "bag_picked"
            }
        },
        {
            "bag_id": 11250,
            "id": 31575,
            "delivery_partner_id": 1,
            "status": "out_for_delivery",
            "delivery_awb_number": "711059984",
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:47:45+00:00",
            "created_at": "2021-04-27T17:47:45+00:00",
            "state_id": 13,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Out For Delivery",
                "app_facing": True,
                "is_active": True,
                "id": 13,
                "notify_customer": True,
                "journey_type": "forward",
                "app_display_name": "Out For Delivery",
                "app_state_name": "out_for_delivery",
                "state_type": "operational",
                "name": "out_for_delivery"
            }
        },
        {
            "bag_id": 11250,
            "id": 31576,
            "delivery_partner_id": 1,
            "status": "delivery_done",
            "delivery_awb_number": "711059984",
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:47:58+00:00",
            "created_at": "2021-04-27T17:47:58+00:00",
            "state_id": 14,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Delivery Done",
                "app_facing": True,
                "is_active": True,
                "id": 14,
                "notify_customer": True,
                "journey_type": "forward",
                "app_display_name": "Delivered",
                "app_state_name": "delivered",
                "state_type": "operational",
                "name": "delivery_done"
            }
        },
        {
            "bag_id": 11250,
            "id": 31577,
            "delivery_partner_id": 1,
            "status": "return_initiated",
            "delivery_awb_number": "711059984",
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:49:32+00:00",
            "created_at": "2021-04-27T17:49:32+00:00",
            "state_id": 26,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Return Initiated",
                "app_facing": True,
                "is_active": True,
                "id": 26,
                "notify_customer": True,
                "journey_type": "return",
                "app_display_name": "Return Processing",
                "app_state_name": "return_processing",
                "state_type": "operational",
                "name": "return_initiated"
            }
        },
        {
            "bag_id": 11250,
            "id": 31578,
            "delivery_partner_id": 1,
            "status": "return_dp_assigned",
            "delivery_awb_number": "503739156",
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:49:33+00:00",
            "created_at": "2021-04-27T17:49:33+00:00",
            "state_id": 41,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Return DP Assigned",
                "app_facing": False,
                "is_active": True,
                "id": 41,
                "notify_customer": False,
                "journey_type": "return",
                "app_display_name": "Return DP Assigned",
                "app_state_name": "return_dp_assigned",
                "state_type": "operational",
                "name": "return_dp_assigned"
            }
        },
        {
            "bag_id": 11250,
            "id": 31579,
            "delivery_partner_id": 1,
            "status": "return_bag_picked",
            "delivery_awb_number": "503739156",
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:50:15+00:00",
            "created_at": "2021-04-27T17:50:15+00:00",
            "state_id": 48,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Return Bag Picked",
                "app_facing": True,
                "is_active": True,
                "id": 48,
                "notify_customer": False,
                "journey_type": "return",
                "app_display_name": "Return Product Picked",
                "app_state_name": "return_product_picked",
                "state_type": "operational",
                "name": "return_bag_picked"
            }
        },
        {
            "bag_id": 11250,
            "id": 31580,
            "delivery_partner_id": 1,
            "status": "refund_initiated",
            "delivery_awb_number": "503739156",
            "state_type": "financial",
            "store_id": 1,
            "updated_at": "2021-04-27T17:50:16+00:00",
            "created_at": "2021-04-27T17:50:16+00:00",
            "state_id": 53,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Refund Initiated",
                "app_facing": False,
                "is_active": True,
                "id": 53,
                "notify_customer": False,
                "journey_type": None,
                "app_display_name": "Refund Initiated ",
                "app_state_name": "refund_initiated",
                "state_type": "financial",
                "name": "refund_initiated"
            }
        },
        {
            "bag_id": 11250,
            "id": 31581,
            "delivery_partner_id": 1,
            "status": "refund_acknowledged",
            "delivery_awb_number": "503739156",
            "state_type": "financial",
            "store_id": 1,
            "updated_at": "2021-04-27T17:50:16+00:00",
            "created_at": "2021-04-27T17:50:16+00:00",
            "state_id": 111,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Refund Acknowledged",
                "app_facing": False,
                "is_active": True,
                "id": 111,
                "notify_customer": False,
                "journey_type": None,
                "app_display_name": "Refund Processed",
                "app_state_name": "refund_acknowledged",
                "state_type": "financial",
                "name": "refund_acknowledged"
            }
        },
        {
            "bag_id": 11250,
            "id": 31582,
            "delivery_partner_id": 1,
            "status": "return_bag_delivered",
            "delivery_awb_number": "503739156",
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:50:31+00:00",
            "created_at": "2021-04-27T17:50:31+00:00",
            "state_id": 50,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Delivery Done to store",
                "app_facing": False,
                "is_active": True,
                "id": 50,
                "notify_customer": False,
                "journey_type": "return",
                "app_display_name": " ",
                "app_state_name": "_",
                "state_type": "operational",
                "name": "return_bag_delivered"
            }
        },
        {
            "bag_id": 11250,
            "id": 31583,
            "delivery_partner_id": 1,
            "status": "return_accepted",
            "delivery_awb_number": "503739156",
            "state_type": "operational",
            "store_id": 1,
            "updated_at": "2021-04-27T17:50:36+00:00",
            "created_at": "2021-04-27T17:50:36+00:00",
            "state_id": 28,
            "kafka_sync": False,
            "bag_state_mapper": {
                "display_name": "Return Accepted",
                "app_facing": True,
                "is_active": True,
                "id": 28,
                "notify_customer": False,
                "journey_type": "return",
                "app_display_name": "Return Accepted",
                "app_state_name": "return_accepted",
                "state_type": "operational",
                "name": "return_accepted"
            }
        }
    ],
    "bags": [
        {
            "id": 11250,
            "display_name": "Bag",
            "entity_type": "bag",
            "type": "single",
            "status": {
                "is_returnable": False,
                "can_be_cancelled": True,
                "enable_tracking": True,
                "is_customer_return_allowed": False,
                "allow_force_return": True,
                "is_active": False
            },
            "financial_breakup": [
                {
                    "price_effective": 115.0,
                    "discount": 15.0,
                    "amount_paid": 115.0,
                    "coupon_effective_discount": 0.0,
                    "delivery_charge": 0.0,
                    "fynd_credits": 0.0,
                    "cod_charges": 0.0,
                    "refund_credit": 0.0,
                    "cashback": 0.0,
                    "refund_amount": 115.0,
                    "added_to_fynd_cash": False,
                    "cashback_applied": 0.0,
                    "gst_tax_percentage": 12.0,
                    "value_of_good": 0.0,
                    "price_marked": 130.0,
                    "transfer_price": 0.0,
                    "brand_calculated_amount": 115.0,
                    "coupon_value": 0.0,
                    "pm_price_split": {
                        "CoD": 115
                    },
                    "size": "",
                    "total_units": 1,
                    "hsn_code": "20081920",
                    "identifiers": {
                        "sku": "RVSQSKQCNM"
                    },
                    "item_name": "Naturoz Roasted Mix Seeds 200g",
                    "gst_fee": "0.0",
                    "gst_tag": "IGST"
                }
            ],
            "bag_id": 11250,
            "bag_update_time": 1619526035.73397,
            "current_status": {
                "bag_id": 11250,
                "id": 31583,
                "delivery_partner_id": 1,
                "status": "return_accepted",
                "delivery_awb_number": "503739156",
                "state_type": "operational",
                "store_id": 1,
                "updated_at": "",  # Date("2021-04-27T17:50:36.000Z"),
                "created_at": "2021-04-27T17:50:36+00:00",
                "state_id": 28,
                "kafka_sync": False,
                "bag_state_mapper": {
                    "display_name": "Return Accepted",
                    "app_facing": True,
                    "is_active": True,
                    "id": 28,
                    "notify_customer": False,
                    "journey_type": "return",
                    "app_display_name": "Return Accepted",
                    "app_state_name": "return_accepted",
                    "state_type": "operational",
                    "name": "return_accepted"
                }
            },
            "bag_status": [
                {
                    "bag_id": 11250,
                    "id": 31567,
                    "delivery_partner_id": None,
                    "status": "pending",
                    "delivery_awb_number": None,
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:45:58.000Z"),
                    "created_at": "2021-04-27T17:45:58+00:00",
                    "state_id": 89,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Pending",
                        "app_facing": True,
                        "is_active": True,
                        "id": 89,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Pending",
                        "app_state_name": "pending",
                        "state_type": "operational",
                        "name": "pending"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31568,
                    "delivery_partner_id": None,
                    "status": "placed",
                    "delivery_awb_number": None,
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:45:58.000Z"),
                    "created_at": "2021-04-27T17:45:58+00:00",
                    "state_id": 1,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Placed",
                        "app_facing": True,
                        "is_active": True,
                        "id": 1,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Ordered",
                        "app_state_name": "processing",
                        "state_type": "operational",
                        "name": "placed"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31569,
                    "delivery_partner_id": None,
                    "status": "bag_confirmed",
                    "delivery_awb_number": None,
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:46:38.000Z"),
                    "created_at": "2021-04-27T17:46:38+00:00",
                    "state_id": 2,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Bag Confirmed",
                        "app_facing": True,
                        "is_active": True,
                        "id": 2,
                        "notify_customer": False,
                        "journey_type": "forward",
                        "app_display_name": "Ordered",
                        "app_state_name": "confirmed",
                        "state_type": "operational",
                        "name": "bag_confirmed"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31570,
                    "delivery_partner_id": None,
                    "status": "bag_invoiced",
                    "delivery_awb_number": None,
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:46:44.000Z"),
                    "created_at": "2021-04-27T17:46:44+00:00",
                    "state_id": 91,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Under Process",
                        "app_facing": True,
                        "is_active": True,
                        "id": 91,
                        "notify_customer": False,
                        "journey_type": "forward",
                        "app_display_name": "Under Process",
                        "app_state_name": "bag_invoiced",
                        "state_type": "operational",
                        "name": "bag_invoiced"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31571,
                    "delivery_partner_id": None,
                    "status": "bag_packed",
                    "delivery_awb_number": None,
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:10.000Z"),
                    "created_at": "2021-04-27T17:47:10+00:00",
                    "state_id": 8,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Bag Packed",
                        "app_facing": True,
                        "is_active": True,
                        "id": 8,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Under Process",
                        "app_state_name": "bag_packed",
                        "state_type": "operational",
                        "name": "bag_packed"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31572,
                    "delivery_partner_id": 1,
                    "status": "dp_assigned",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:11.000Z"),
                    "created_at": "2021-04-27T17:47:11+00:00",
                    "state_id": 7,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "DP Assigned",
                        "app_facing": False,
                        "is_active": True,
                        "id": 7,
                        "notify_customer": False,
                        "journey_type": "forward",
                        "app_display_name": "DP Assigned",
                        "app_state_name": "dp_assigned",
                        "state_type": "operational",
                        "name": "dp_assigned"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31573,
                    "delivery_partner_id": 1,
                    "status": "handed_over_to_dg",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:20.000Z"),
                    "created_at": "2021-04-27T17:47:20+00:00",
                    "state_id": 10,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Handed Over to DG",
                        "app_facing": True,
                        "is_active": True,
                        "id": 10,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Under Process",
                        "app_state_name": "bag_packed",
                        "state_type": "operational",
                        "name": "handed_over_to_dg"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31574,
                    "delivery_partner_id": 1,
                    "status": "bag_picked",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:33.000Z"),
                    "created_at": "2021-04-27T17:47:33+00:00",
                    "state_id": 12,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "In Transit",
                        "app_facing": True,
                        "is_active": True,
                        "id": 12,
                        "notify_customer": False,
                        "journey_type": "forward",
                        "app_display_name": "Shipped",
                        "app_state_name": "in_transit",
                        "state_type": "operational",
                        "name": "bag_picked"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31575,
                    "delivery_partner_id": 1,
                    "status": "out_for_delivery",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:45.000Z"),
                    "created_at": "2021-04-27T17:47:45+00:00",
                    "state_id": 13,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Out For Delivery",
                        "app_facing": True,
                        "is_active": True,
                        "id": 13,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Out For Delivery",
                        "app_state_name": "out_for_delivery",
                        "state_type": "operational",
                        "name": "out_for_delivery"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31576,
                    "delivery_partner_id": 1,
                    "status": "delivery_done",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:58.000Z"),
                    "created_at": "2021-04-27T17:47:58+00:00",
                    "state_id": 14,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Delivery Done",
                        "app_facing": True,
                        "is_active": True,
                        "id": 14,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Delivered",
                        "app_state_name": "delivered",
                        "state_type": "operational",
                        "name": "delivery_done"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31577,
                    "delivery_partner_id": 1,
                    "status": "return_initiated",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:49:32.000Z"),
                    "created_at": "2021-04-27T17:49:32+00:00",
                    "state_id": 26,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Return Initiated",
                        "app_facing": True,
                        "is_active": True,
                        "id": 26,
                        "notify_customer": True,
                        "journey_type": "return",
                        "app_display_name": "Return Processing",
                        "app_state_name": "return_processing",
                        "state_type": "operational",
                        "name": "return_initiated"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31578,
                    "delivery_partner_id": 1,
                    "status": "return_dp_assigned",
                    "delivery_awb_number": "503739156",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:49:33.000Z"),
                    "created_at": "2021-04-27T17:49:33+00:00",
                    "state_id": 41,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Return DP Assigned",
                        "app_facing": False,
                        "is_active": True,
                        "id": 41,
                        "notify_customer": False,
                        "journey_type": "return",
                        "app_display_name": "Return DP Assigned",
                        "app_state_name": "return_dp_assigned",
                        "state_type": "operational",
                        "name": "return_dp_assigned"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31579,
                    "delivery_partner_id": 1,
                    "status": "return_bag_picked",
                    "delivery_awb_number": "503739156",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:50:15.000Z"),
                    "created_at": "2021-04-27T17:50:15+00:00",
                    "state_id": 48,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Return Bag Picked",
                        "app_facing": True,
                        "is_active": True,
                        "id": 48,
                        "notify_customer": False,
                        "journey_type": "return",
                        "app_display_name": "Return Product Picked",
                        "app_state_name": "return_product_picked",
                        "state_type": "operational",
                        "name": "return_bag_picked"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31580,
                    "delivery_partner_id": 1,
                    "status": "refund_initiated",
                    "delivery_awb_number": "503739156",
                    "state_type": "financial",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:50:16.000Z"),
                    "created_at": "2021-04-27T17:50:16+00:00",
                    "state_id": 53,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Refund Initiated",
                        "app_facing": False,
                        "is_active": True,
                        "id": 53,
                        "notify_customer": False,
                        "journey_type": None,
                        "app_display_name": "Refund Initiated ",
                        "app_state_name": "refund_initiated",
                        "state_type": "financial",
                        "name": "refund_initiated"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31581,
                    "delivery_partner_id": 1,
                    "status": "refund_acknowledged",
                    "delivery_awb_number": "503739156",
                    "state_type": "financial",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:50:16.000Z"),
                    "created_at": "2021-04-27T17:50:16+00:00",
                    "state_id": 111,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Refund Acknowledged",
                        "app_facing": False,
                        "is_active": True,
                        "id": 111,
                        "notify_customer": False,
                        "journey_type": None,
                        "app_display_name": "Refund Processed",
                        "app_state_name": "refund_acknowledged",
                        "state_type": "financial",
                        "name": "refund_acknowledged"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31582,
                    "delivery_partner_id": 1,
                    "status": "return_bag_delivered",
                    "delivery_awb_number": "503739156",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:50:31.000Z"),
                    "created_at": "2021-04-27T17:50:31+00:00",
                    "state_id": 50,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Delivery Done to store",
                        "app_facing": False,
                        "is_active": True,
                        "id": 50,
                        "notify_customer": False,
                        "journey_type": "return",
                        "app_display_name": " ",
                        "app_state_name": "_",
                        "state_type": "operational",
                        "name": "return_bag_delivered"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31583,
                    "delivery_partner_id": 1,
                    "status": "return_accepted",
                    "delivery_awb_number": "503739156",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:50:36.000Z"),
                    "created_at": "2021-04-27T17:50:36+00:00",
                    "state_id": 28,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Return Accepted",
                        "app_facing": True,
                        "is_active": True,
                        "id": 28,
                        "notify_customer": False,
                        "journey_type": "return",
                        "app_display_name": "Return Accepted",
                        "app_state_name": "return_accepted",
                        "state_type": "operational",
                        "name": "return_accepted"
                    }
                }
            ],
            "item": {
                "code": "RVSQSKQCNM",
                "l1_category": None,
                "slug_key": None,
                "id": 98,
                "color": None,
                "brand": "Naturoz",
                "l2_category": None,
                "l3_category_name": "Home,Groceries,Staples,Dry Fruits & Nuts,Dried Seeds",
                "can_return": False,
                "gender": None,
                "webstore_product_url": None,
                "last_updated_at": "",  # Date("2021-02-18T01:27:22.000Z"),
                "name": "Naturoz Roasted Mix Seeds 200g",
                "can_cancel": True,
                "attributes": {
                    "dimensions": {
                        "item_dimensions": {
                            "depth": {
                                "unit": None,
                                "value": 0
                            },
                            "width": {
                                "unit": None,
                                "value": 0
                            },
                            "height": {
                                "unit": None,
                                "value": 0
                            },
                            "length": {
                                "unit": None,
                                "value": 0
                            },
                            "volume": {
                                "unit": None,
                                "value": 0
                            },
                            "net_weight": {
                                "unit": "kilogram",
                                "value": 0.2
                            }
                        },
                        "package_dimensions": {
                            "depth": {
                                "unit": None,
                                "value": 0
                            },
                            "width": {
                                "unit": "centimeter",
                                "value": 4.5
                            },
                            "height": {
                                "unit": "centimeter",
                                "value": 3
                            },
                            "length": {
                                "unit": "centimeter",
                                "value": 21
                            },
                            "gross_weight": {
                                "unit": "kilogram",
                                "value": 0.2
                            },
                            "volumetric_weight": {
                                "unit": None,
                                "value": 0
                            }
                        }
                    }
                },
                "branch_url": None,
                "l3_category": None,
                "size": "",
                "image": [
                    "https://sit-eks-pixed.ril.smebazaar.ooo/img/c/images/othe/7607154/.p/ng/naturoz20roasted20seeds20mix20no20salt20200g20front.png.7sfc.999xx.png"
                ]
            },
            "reasons": [
                {
                    "slug": "card_issues",
                    "display_name": "Card issues",
                    "id": 4,
                    "state": "accept_buy_request",
                    "text": None,
                    "bag_id": 11250
                }
            ],
            "article": {
                "identifiers": {
                    "sku": "RVSQSKQCNM"
                },
                "esp_modified": "",
                "size": "",
                "code": "",
                "raw_meta": None,
                "set": {},
                "is_set": "",
                "seller_identifier": "RVSQSKQCNM",
                "_id": "",
                "uid": "rvsqskqcnm"
            },
            "journey_type": "return",
            "current_operational_status": {
                "bag_id": 11250,
                "id": 31583,
                "delivery_partner_id": 1,
                "status": "return_accepted",
                "delivery_awb_number": "503739156",
                "state_type": "operational",
                "store_id": 1,
                "updated_at": "2021-04-27T17:50:36+00:00",
                "created_at": "2021-04-27T17:50:36+00:00",
                "state_id": 28,
                "kafka_sync": False,
                "bag_state_mapper": {
                    "display_name": "Return Accepted",
                    "app_facing": True,
                    "is_active": True,
                    "id": 28,
                    "notify_customer": False,
                    "journey_type": "return",
                    "app_display_name": "Return Accepted",
                    "app_state_name": "return_accepted",
                    "state_type": "operational",
                    "name": "return_accepted"
                }
            },
            "dates": {
                "order_created": "2021-04-27T17:45:58+00:00",
                "delivery_date": "2021-04-27T17:47:58+00:00"
            },
            "prices": {
                "price_effective": 115.0,
                "discount": 15.0,
                "amount_paid": 115.0,
                "coupon_effective_discount": 0.0,
                "delivery_charge": 0.0,
                "fynd_credits": 0.0,
                "cod_charges": 0.0,
                "refund_credit": 0.0,
                "cashback": 0.0,
                "refund_amount": 115.0,
                "added_to_fynd_cash": False,
                "cashback_applied": 0.0,
                "gst_tax_percentage": 12.0,
                "value_of_good": 0.0,
                "price_marked": 130.0,
                "transfer_price": 0.0,
                "brand_calculated_amount": 115.0,
                "coupon_value": 0.0,
                "pm_price_split": {
                    "CoD": 115
                }
            },
            "gst_details": {
                "gstin_code": "27AAHCM2029B1ZW",
                "gst_tag": "IGST",
                "hsn_code": "20081920",
                "value_of_good": 0.0,
                "gst_tax_percentage": 12.0,
                "is_default_hsn_code": True,
                "brand_calculated_amount": 115.0,
                "gst_fee": "0.0"
            },
            "brand": {
                "is_virtual_invoice": False,
                "start_date": None,
                "id": 11,
                "pickup_location": None,
                "created_on": "",  # Date("2021-02-17T19:57:23.000Z"),
                "credit_note_expiry_days": None,
                "script_last_ran": None,
                "modified_on": "",  # Date("2021-02-17T19:57:23.000Z"),
                "invoice_prefix": None,
                "brand_name": "Naturoz",
                "credit_note_allowed": False,
                "logo": None,
                "company": None
            },
            "affiliate_bag_details": {
                "affiliate_bag_id": None,
                "affiliate_order_id": "16195257569000112W",
                "affiliate_meta": {
                    "fynd": {
                        "fulfilment_identifier": "infibeam"
                    }
                },
                "loyalty_discount": 0.0,
                "employee_discount": 0.0
            },
            "meta": {
                "sku": "RVSQSKQCNM",
                "name": None,
                "prices": {
                    "esp": 115,
                    "mrp": 130,
                    "meta": {},
                    "amount_paid": 115,
                    "cod_charges": 0,
                    "coupon_json": {},
                    "price_marked": 130,
                    "refund_amount": 115,
                    "promo_discount": 0,
                    "coupon_discount": 0,
                    "price_effective": 115,
                    "delivery_charges": 0,
                    "product_discount": 15,
                    "margin_percentage": 0,
                    "brand_coupon_discount": 0,
                    "brand_calculated_amount": 115
                },
                "fulfillment_type": "SMART",
                "product_category": None,
                "supporting_documents": None
            }
        }
    ],
    "bank_data": {
        "penny_validation": False
    },
    "brand": {
        "is_virtual_invoice": False,
        "start_date": None,
        "id": 11,
        "pickup_location": None,
        "created_on": "",  # Date("2021-02-17T19:57:23.000Z"),
        "credit_note_expiry_days": None,
        "script_last_ran": None,
        "modified_on": "",  # Date("2021-02-17T19:57:23.000Z"),
        "invoice_prefix": None,
        "brand_name": "Naturoz",
        "credit_note_allowed": False,
        "logo": None,
        "company": None
    },
    "cart_id": None,
    "comment": "",
    "company": {
        "created_on": "",  # Date("1970-01-01T00:00:00.000Z"),
        "company_name": "asdasdasd",
        "tan_no": None,
        "return_within_days": None,
        "meta": None,
        "agreement_start_date": "",  # Date("1970-01-01T00:00:00.000Z"),
        "vat_no": None,
        "modified_on": "",  # Date("1970-01-01T00:00:00.000Z"),
        "fynd_a_fit_available": None,
        "exchange_allowed": None,
        "business_type": "",
        "return_allowed": None,
        "payment_procesing_charge": None,
        "pan_no": None,
        "exchange_within_days": None,
        "id": 1,
        "company_type": "",
        "cst": None,
        "commission": None,
        "gst_number": "",
        "payment_type": None
    },
    "coupon": {},
    "delivery_address": {
        "area": "",
        "city": "Thane",
        "name": "Priyanjali",
        "email": "",
        "phone": "9890682272",
        "state": "Maharashtra",
        "sector": "Thane",
        "street": "billing address",
        "flat_no": "No. 7",
        "pincode": "421303",
        "plot_no": "",
        "version": "1.0",
        "address1": " No. 7 test building name billing address Thane",
        "block_no": "",
        "floor_no": "",
        "latitude": 19.6639814,
        "tower_no": "test",
        "longitude": 73.2347815,
        "created_at": "2021-04-27T17:45:57+00:00",
        "updated_at": "2021-04-27T17:45:57+00:00",
        "address_type": "home",
        "apartment_id": None,
        "society_name": "",
        "building_name": "building name",
        "contact_person": "Priyanjali",
        "address_other_type": "",
        "delivery_address_id": None,
        "addressee_name": "Priyanjali",
        "address_category": "",
        "landmark": ""
    },
    "delivery_slot": {
        "slot": "By 12:00 PM",
        "upper_bound": "2021-05-08T12:15:39+00:00",
        "lower_bound": "2021-05-04T12:15:39+00:00",
        "date": "2021-05-08T12:15:39+00:00",
        "type": "order_window"
    },
    "dp_details": {
        "id": 1,
        "name": "ecom_jio",
        "awb_no": "503739156",
        "eway_bill_id": None,
        "track_url": None,
        "dp_charges": 110,
        "dp_return_charges": 70,
        "amount_handling_charges": 15,
        "gst_tag": "sgst"
    },
    "fallback_user": {
        "email": "",
        "mobile": ""
    },
    "fulfilling_store": {
        "updated_at": "2020-06-01T13:27:39+00:00",
        "is_enabled_for_recon": False,
        "alohomora_user_id": None,
        "is_archived": False,
        "fulfillment_channel": "infibeam",
        "meta": {
            "stage": "verified",
            "timing": [
                {
                    "open": True,
                    "closing": {
                        "hour": 21,
                        "minute": 0
                    },
                    "opening": {
                        "hour": 11,
                        "minute": 0
                    },
                    "weekday": "monday"
                },
                {
                    "open": True,
                    "closing": {
                        "hour": 21,
                        "minute": 0
                    },
                    "opening": {
                        "hour": 11,
                        "minute": 0
                    },
                    "weekday": "tuesday"
                },
                {
                    "open": True,
                    "closing": {
                        "hour": 21,
                        "minute": 0
                    },
                    "opening": {
                        "hour": 11,
                        "minute": 0
                    },
                    "weekday": "wednesday"
                },
                {
                    "open": True,
                    "closing": {
                        "hour": 18,
                        "minute": 52
                    },
                    "opening": {
                        "hour": 11,
                        "minute": 0
                    },
                    "weekday": "thursday"
                },
                {
                    "open": True,
                    "closing": {
                        "hour": 21,
                        "minute": 0
                    },
                    "opening": {
                        "hour": 11,
                        "minute": 0
                    },
                    "weekday": "friday"
                },
                {
                    "open": True,
                    "closing": {
                        "hour": 21,
                        "minute": 0
                    },
                    "opening": {
                        "hour": 11,
                        "minute": 0
                    },
                    "weekday": "saturday"
                },
                {
                    "open": True,
                    "closing": {
                        "hour": 21,
                        "minute": 0
                    },
                    "opening": {
                        "hour": 11,
                        "minute": 0
                    },
                    "weekday": "sunday"
                }
            ],
            "gst_number": "27AAHCM2029B1ZW",
            "display_name": "Tulsi Dry Fruits",
            "notification_emails": [
                ""
            ],
            "additional_contact_details": {
                "number": [
                    "91 - 7456123456"
                ]
            },
            "allow_dp_assignment_from_fynd": False
        },
        "parent_store_id": None,
        "vat_no": None,
        "company_id": 1,
        "name": "Tulsi Dry Fruits",
        "code": "7352",
        "packaging_material_count": 0,
        "latitude": None,
        "longitude": None,
        "id": 1,
        "is_active": False,
        "mall_name": None,
        "store_address_json": {
            "area": "",
            "city": "NAVI MUMBAI",
            "email": "beinghuman.rcity@mahnada.com",
            "phone": "91000000000",
            "state": "Delhi",
            "country": "INDIA",
            "pincode": "110035",
            "version": "1.0",
            "address1": "B-57,Lawrence Road Industrial Area",
            "address2": "Near Seven Heaven Banquet Hall",
            "landmark": "",
            "latitude": 19.151343,
            "longitude": 73.009313,
            "created_at": "2020-06-29 20:34:04",
            "updated_at": "2020-06-29 20:34:04",
            "address_type": "store",
            "contact_person": "Salma",
            "address_category": "store"
        },
        "store_active_from": None,
        "login_username": "beinghuman.rcity_MRVLB01_1",
        "created_at": "2015-10-15T15:25:03+00:00",
        "brand_id": None,
        "location_type": "mall",
        "mall_area": None,
        "address1": "B-57,Lawrence Road Industrial Area",
        "address2": "Near Seven Heaven Banquet Hall",
        "city": "NAVI MUMBAI",
        "state": "Delhi",
        "country": "INDIA",
        "pincode": "110035",
        "store_email": "beinghuman.rcity@mahnada.com",
        "contact_person": "Salma",
        "phone": "91000000000",
        "brand_store_tags": [
            "infibeam"
        ]
    },
    "fyndstore_emp": {},
    "invoice": {
        "updated_date": "",  # Date("2021-04-27T17:46:44.000Z"),
        "store_invoice_id": "JS29GY9OFWBA00018",
        "invoice_url": "",
        "label_url": ""
    },
    "is_processing": False,
    "journey_type": "return",
    "lock_status": False,
    "no_of_bags_order": 1,
    "operational_status": "return_accepted",
    "order": {
        "cashback_value": 0.0,
        "fynd_credits": 0.0,
        "mongo_cart_id": 1000000007,
        "coupon_value": None,
        "meta": {
            "staff": {},
            "prices": {
                "order_type": "COD",
                "cod_charges": 0,
                "gross_total": 130,
                "tax_details": {
                    "gstin": None
                },
                "final_amount": 115,
                "cashback_value": 0,
                "delivery_charges": 0,
                "total_order_discount": 15,
                "total_promo_discount": 0,
                "total_coupon_discount": 0,
                "total_product_discount": 15
            },
            "comment": "",
            "channel_id": "web",
            "extra_meta": {},
            "order_type": "HomeDelivery",
            "employee_id": "",
            "payment_type": None,
            "ordering_store": None
        },
        "source": "NA",
        "total_order_value": 130.0,
        "created_time": "",  # Date("2021-04-27T17:45:58.000Z"),
        "tax_details": {
            "gstin": "NA"
        },
        "affiliate_id": "5ea6821b3425bb07c82a25c1",
        "payment_mode_id": None,
        "fynd_order_id": "FYMP6088007D18A64C7B",
        "cod_charges": 0,
        "affiliate_order_date": "2021-04-27T17:45:56+00:00",
        "mode_of_payment": "JIOMART",
        "user_id": 23,
        "id": 41473,
        "cashback_applied": 0.0,
        "delivery_charges": 0.0,
        "discount": 15.0,
        "order_value": 130.0,
        "ordering_channel": "JIOMART",
        "affiliate_order_id": "16195257569000112W",
        "currency": "INR",
        "ordering_channel_logo": None,
        "prices": {
            "amount_paid": 115.0,
            "refund_amount": 115.0,
            "price_marked": 130.0,
            "cod_charges": 0.0,
            "discount": 15.0,
            "cashback_applied": 0.0,
            "delivery_charge": 0.0,
            "fynd_credits": 0.0,
            "cashback": 0.0,
            "price_effective": 115.0,
            "refund_credit": 0.0,
            "value_of_good": 0.0,
            "pm_price_split": {
                "CoD": 115
            },
            "brand_calculated_amount": 115.0,
            "coupon_effective_discount": 0.0,
            "coupon_value": 0.0
        }
    },
    "order_source": "NA",
    "order_type": "return",
    "order_value": 130.0,
    "ordering_store": {},
    "original_bag_list": [
        11250
    ],
    "payment_methods": [
        {
            "slug": "Prepaid_payments",
            "txn_date": "2021-04-27T17:45:56",
            "payment_id": "20",
            "payment_amt": 115.0,
            "payment_cart": None,
            "payment_desc": "CoD",
            "bdcustomer_id": None,
            "order_inv_num": None,
            "order_app_code": None,
            "mode_of_payment": "PREPAID",
            "payment_gateway_logo": None,
            "transaction_ref_number": "-NA- (cod)"
        }
    ],
    "payment_mode": "COD",
    "payment_type": None,
    "payments": {
        "mode": "COD"
    },
    "prices": {
        "amount_paid": 115.0,
        "refund_amount": 115.0,
        "price_marked": 130.0,
        "cod_charges": 0.0,
        "discount": 15.0,
        "cashback_applied": 0.0,
        "delivery_charge": 0.0,
        "fynd_credits": 0.0,
        "cashback": 0.0,
        "price_effective": 115.0,
        "refund_credit": 0.0,
        "value_of_good": 0.0,
        "pm_price_split": {
            "CoD": 115
        },
        "brand_calculated_amount": 115.0,
        "coupon_effective_discount": 0.0
    },
    "products": [
        {
            "id": 11250,
            "display_name": "Bag",
            "entity_type": "bag",
            "type": "single",
            "status": {
                "is_returnable": False,
                "can_be_cancelled": True,
                "enable_tracking": True,
                "is_customer_return_allowed": False,
                "allow_force_return": True,
                "is_active": False
            },
            "financial_breakup": [
                {
                    "price_effective": 115.0,
                    "discount": 15.0,
                    "amount_paid": 115.0,
                    "coupon_effective_discount": 0.0,
                    "delivery_charge": 0.0,
                    "fynd_credits": 0.0,
                    "cod_charges": 0.0,
                    "refund_credit": 0.0,
                    "cashback": 0.0,
                    "refund_amount": 115.0,
                    "added_to_fynd_cash": False,
                    "cashback_applied": 0.0,
                    "gst_tax_percentage": 12.0,
                    "value_of_good": 0.0,
                    "price_marked": 130.0,
                    "transfer_price": 0.0,
                    "brand_calculated_amount": 115.0,
                    "coupon_value": 0.0,
                    "pm_price_split": {
                        "CoD": 115
                    },
                    "size": "",
                    "total_units": 1,
                    "hsn_code": "20081920",
                    "identifiers": {
                        "sku": "RVSQSKQCNM"
                    },
                    "item_name": "Naturoz Roasted Mix Seeds 200g",
                    "gst_fee": "0.0",
                    "gst_tag": "IGST"
                }
            ],
            "bag_id": 11250,
            "bag_update_time": 1619526035.73397,
            "current_status": {
                "bag_id": 11250,
                "id": 31583,
                "delivery_partner_id": 1,
                "status": "return_accepted",
                "delivery_awb_number": "503739156",
                "state_type": "operational",
                "store_id": 1,
                "updated_at": "",  # Date("2021-04-27T17:50:36.000Z"),
                "created_at": "2021-04-27T17:50:36+00:00",
                "state_id": 28,
                "kafka_sync": False,
                "bag_state_mapper": {
                    "display_name": "Return Accepted",
                    "app_facing": True,
                    "is_active": True,
                    "id": 28,
                    "notify_customer": False,
                    "journey_type": "return",
                    "app_display_name": "Return Accepted",
                    "app_state_name": "return_accepted",
                    "state_type": "operational",
                    "name": "return_accepted"
                }
            },
            "bag_status": [
                {
                    "bag_id": 11250,
                    "id": 31567,
                    "delivery_partner_id": None,
                    "status": "pending",
                    "delivery_awb_number": None,
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:45:58.000Z"),
                    "created_at": "2021-04-27T17:45:58+00:00",
                    "state_id": 89,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Pending",
                        "app_facing": True,
                        "is_active": True,
                        "id": 89,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Pending",
                        "app_state_name": "pending",
                        "state_type": "operational",
                        "name": "pending"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31568,
                    "delivery_partner_id": None,
                    "status": "placed",
                    "delivery_awb_number": None,
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:45:58.000Z"),
                    "created_at": "2021-04-27T17:45:58+00:00",
                    "state_id": 1,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Placed",
                        "app_facing": True,
                        "is_active": True,
                        "id": 1,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Ordered",
                        "app_state_name": "processing",
                        "state_type": "operational",
                        "name": "placed"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31569,
                    "delivery_partner_id": None,
                    "status": "bag_confirmed",
                    "delivery_awb_number": None,
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:46:38.000Z"),
                    "created_at": "2021-04-27T17:46:38+00:00",
                    "state_id": 2,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Bag Confirmed",
                        "app_facing": True,
                        "is_active": True,
                        "id": 2,
                        "notify_customer": False,
                        "journey_type": "forward",
                        "app_display_name": "Ordered",
                        "app_state_name": "confirmed",
                        "state_type": "operational",
                        "name": "bag_confirmed"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31570,
                    "delivery_partner_id": None,
                    "status": "bag_invoiced",
                    "delivery_awb_number": None,
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:46:44.000Z"),
                    "created_at": "2021-04-27T17:46:44+00:00",
                    "state_id": 91,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Under Process",
                        "app_facing": True,
                        "is_active": True,
                        "id": 91,
                        "notify_customer": False,
                        "journey_type": "forward",
                        "app_display_name": "Under Process",
                        "app_state_name": "bag_invoiced",
                        "state_type": "operational",
                        "name": "bag_invoiced"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31571,
                    "delivery_partner_id": None,
                    "status": "bag_packed",
                    "delivery_awb_number": None,
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:10.000Z"),
                    "created_at": "2021-04-27T17:47:10+00:00",
                    "state_id": 8,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Bag Packed",
                        "app_facing": True,
                        "is_active": True,
                        "id": 8,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Under Process",
                        "app_state_name": "bag_packed",
                        "state_type": "operational",
                        "name": "bag_packed"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31572,
                    "delivery_partner_id": 1,
                    "status": "dp_assigned",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:11.000Z"),
                    "created_at": "2021-04-27T17:47:11+00:00",
                    "state_id": 7,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "DP Assigned",
                        "app_facing": False,
                        "is_active": True,
                        "id": 7,
                        "notify_customer": False,
                        "journey_type": "forward",
                        "app_display_name": "DP Assigned",
                        "app_state_name": "dp_assigned",
                        "state_type": "operational",
                        "name": "dp_assigned"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31573,
                    "delivery_partner_id": 1,
                    "status": "handed_over_to_dg",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:20.000Z"),
                    "created_at": "2021-04-27T17:47:20+00:00",
                    "state_id": 10,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Handed Over to DG",
                        "app_facing": True,
                        "is_active": True,
                        "id": 10,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Under Process",
                        "app_state_name": "bag_packed",
                        "state_type": "operational",
                        "name": "handed_over_to_dg"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31574,
                    "delivery_partner_id": 1,
                    "status": "bag_picked",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:33.000Z"),
                    "created_at": "2021-04-27T17:47:33+00:00",
                    "state_id": 12,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "In Transit",
                        "app_facing": True,
                        "is_active": True,
                        "id": 12,
                        "notify_customer": False,
                        "journey_type": "forward",
                        "app_display_name": "Shipped",
                        "app_state_name": "in_transit",
                        "state_type": "operational",
                        "name": "bag_picked"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31575,
                    "delivery_partner_id": 1,
                    "status": "out_for_delivery",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:45.000Z"),
                    "created_at": "2021-04-27T17:47:45+00:00",
                    "state_id": 13,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Out For Delivery",
                        "app_facing": True,
                        "is_active": True,
                        "id": 13,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Out For Delivery",
                        "app_state_name": "out_for_delivery",
                        "state_type": "operational",
                        "name": "out_for_delivery"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31576,
                    "delivery_partner_id": 1,
                    "status": "delivery_done",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:47:58.000Z"),
                    "created_at": "2021-04-27T17:47:58+00:00",
                    "state_id": 14,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Delivery Done",
                        "app_facing": True,
                        "is_active": True,
                        "id": 14,
                        "notify_customer": True,
                        "journey_type": "forward",
                        "app_display_name": "Delivered",
                        "app_state_name": "delivered",
                        "state_type": "operational",
                        "name": "delivery_done"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31577,
                    "delivery_partner_id": 1,
                    "status": "return_initiated",
                    "delivery_awb_number": "711059984",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:49:32.000Z"),
                    "created_at": "2021-04-27T17:49:32+00:00",
                    "state_id": 26,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Return Initiated",
                        "app_facing": True,
                        "is_active": True,
                        "id": 26,
                        "notify_customer": True,
                        "journey_type": "return",
                        "app_display_name": "Return Processing",
                        "app_state_name": "return_processing",
                        "state_type": "operational",
                        "name": "return_initiated"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31578,
                    "delivery_partner_id": 1,
                    "status": "return_dp_assigned",
                    "delivery_awb_number": "503739156",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:49:33.000Z"),
                    "created_at": "2021-04-27T17:49:33+00:00",
                    "state_id": 41,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Return DP Assigned",
                        "app_facing": False,
                        "is_active": True,
                        "id": 41,
                        "notify_customer": False,
                        "journey_type": "return",
                        "app_display_name": "Return DP Assigned",
                        "app_state_name": "return_dp_assigned",
                        "state_type": "operational",
                        "name": "return_dp_assigned"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31579,
                    "delivery_partner_id": 1,
                    "status": "return_bag_picked",
                    "delivery_awb_number": "503739156",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:50:15.000Z"),
                    "created_at": "2021-04-27T17:50:15+00:00",
                    "state_id": 48,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Return Bag Picked",
                        "app_facing": True,
                        "is_active": True,
                        "id": 48,
                        "notify_customer": False,
                        "journey_type": "return",
                        "app_display_name": "Return Product Picked",
                        "app_state_name": "return_product_picked",
                        "state_type": "operational",
                        "name": "return_bag_picked"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31580,
                    "delivery_partner_id": 1,
                    "status": "refund_initiated",
                    "delivery_awb_number": "503739156",
                    "state_type": "financial",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:50:16.000Z"),
                    "created_at": "2021-04-27T17:50:16+00:00",
                    "state_id": 53,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Refund Initiated",
                        "app_facing": False,
                        "is_active": True,
                        "id": 53,
                        "notify_customer": False,
                        "journey_type": None,
                        "app_display_name": "Refund Initiated ",
                        "app_state_name": "refund_initiated",
                        "state_type": "financial",
                        "name": "refund_initiated"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31581,
                    "delivery_partner_id": 1,
                    "status": "refund_acknowledged",
                    "delivery_awb_number": "503739156",
                    "state_type": "financial",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:50:16.000Z"),
                    "created_at": "2021-04-27T17:50:16+00:00",
                    "state_id": 111,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Refund Acknowledged",
                        "app_facing": False,
                        "is_active": True,
                        "id": 111,
                        "notify_customer": False,
                        "journey_type": None,
                        "app_display_name": "Refund Processed",
                        "app_state_name": "refund_acknowledged",
                        "state_type": "financial",
                        "name": "refund_acknowledged"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31582,
                    "delivery_partner_id": 1,
                    "status": "return_bag_delivered",
                    "delivery_awb_number": "503739156",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:50:31.000Z"),
                    "created_at": "2021-04-27T17:50:31+00:00",
                    "state_id": 50,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Delivery Done to store",
                        "app_facing": False,
                        "is_active": True,
                        "id": 50,
                        "notify_customer": False,
                        "journey_type": "return",
                        "app_display_name": " ",
                        "app_state_name": "_",
                        "state_type": "operational",
                        "name": "return_bag_delivered"
                    }
                },
                {
                    "bag_id": 11250,
                    "id": 31583,
                    "delivery_partner_id": 1,
                    "status": "return_accepted",
                    "delivery_awb_number": "503739156",
                    "state_type": "operational",
                    "store_id": 1,
                    "updated_at": "",  # Date("2021-04-27T17:50:36.000Z"),
                    "created_at": "2021-04-27T17:50:36+00:00",
                    "state_id": 28,
                    "kafka_sync": False,
                    "bag_state_mapper": {
                        "display_name": "Return Accepted",
                        "app_facing": True,
                        "is_active": True,
                        "id": 28,
                        "notify_customer": False,
                        "journey_type": "return",
                        "app_display_name": "Return Accepted",
                        "app_state_name": "return_accepted",
                        "state_type": "operational",
                        "name": "return_accepted"
                    }
                }
            ],
            "item": {
                "code": "RVSQSKQCNM",
                "l1_category": None,
                "slug_key": None,
                "id": 98,
                "color": None,
                "brand": "Naturoz",
                "l2_category": None,
                "l3_category_name": "Home,Groceries,Staples,Dry Fruits & Nuts,Dried Seeds",
                "can_return": False,
                "gender": None,
                "webstore_product_url": None,
                "last_updated_at": "",  # Date("2021-02-18T01:27:22.000Z"),
                "name": "Naturoz Roasted Mix Seeds 200g",
                "can_cancel": True,
                "attributes": {
                    "dimensions": {
                        "item_dimensions": {
                            "depth": {
                                "unit": None,
                                "value": 0
                            },
                            "width": {
                                "unit": None,
                                "value": 0
                            },
                            "height": {
                                "unit": None,
                                "value": 0
                            },
                            "length": {
                                "unit": None,
                                "value": 0
                            },
                            "volume": {
                                "unit": None,
                                "value": 0
                            },
                            "net_weight": {
                                "unit": "kilogram",
                                "value": 0.2
                            }
                        },
                        "package_dimensions": {
                            "depth": {
                                "unit": None,
                                "value": 0
                            },
                            "width": {
                                "unit": "centimeter",
                                "value": 4.5
                            },
                            "height": {
                                "unit": "centimeter",
                                "value": 3
                            },
                            "length": {
                                "unit": "centimeter",
                                "value": 21
                            },
                            "gross_weight": {
                                "unit": "kilogram",
                                "value": 0.2
                            },
                            "volumetric_weight": {
                                "unit": None,
                                "value": 0
                            }
                        }
                    }
                },
                "branch_url": None,
                "l3_category": None,
                "size": "",
                "image": [
                    "https://sit-eks-pixed.ril.smebazaar.ooo/img/c/images/othe/7607154/.p/ng/naturoz20roasted20seeds20mix20no20salt20200g20front.png.7sfc.999xx.png"
                ]
            },
            "reasons": [
                {
                    "slug": "card_issues",
                    "display_name": "Card issues",
                    "id": 4,
                    "state": "accept_buy_request",
                    "text": None,
                    "bag_id": 11250
                }
            ],
            "article": {
                "identifiers": {
                    "sku": "RVSQSKQCNM"
                },
                "esp_modified": "",
                "size": "",
                "code": "",
                "raw_meta": None,
                "set": {},
                "is_set": "",
                "seller_identifier": "RVSQSKQCNM",
                "_id": "",
                "uid": "rvsqskqcnm"
            },
            "journey_type": "return",
            "current_operational_status": {
                "bag_id": 11250,
                "id": 31583,
                "delivery_partner_id": 1,
                "status": "return_accepted",
                "delivery_awb_number": "503739156",
                "state_type": "operational",
                "store_id": 1,
                "updated_at": "2021-04-27T17:50:36+00:00",
                "created_at": "2021-04-27T17:50:36+00:00",
                "state_id": 28,
                "kafka_sync": False,
                "bag_state_mapper": {
                    "display_name": "Return Accepted",
                    "app_facing": True,
                    "is_active": True,
                    "id": 28,
                    "notify_customer": False,
                    "journey_type": "return",
                    "app_display_name": "Return Accepted",
                    "app_state_name": "return_accepted",
                    "state_type": "operational",
                    "name": "return_accepted"
                }
            },
            "dates": {
                "order_created": "2021-04-27T17:45:58+00:00",
                "delivery_date": "2021-04-27T17:47:58+00:00"
            },
            "prices": {
                "price_effective": 115.0,
                "discount": 15.0,
                "amount_paid": 115.0,
                "coupon_effective_discount": 0.0,
                "delivery_charge": 0.0,
                "fynd_credits": 0.0,
                "cod_charges": 0.0,
                "refund_credit": 0.0,
                "cashback": 0.0,
                "refund_amount": 115.0,
                "added_to_fynd_cash": False,
                "cashback_applied": 0.0,
                "gst_tax_percentage": 12.0,
                "value_of_good": 0.0,
                "price_marked": 130.0,
                "transfer_price": 0.0,
                "brand_calculated_amount": 115.0,
                "coupon_value": 0.0,
                "pm_price_split": {
                    "CoD": 115
                }
            },
            "gst_details": {
                "gstin_code": "27AAHCM2029B1ZW",
                "gst_tag": "IGST",
                "hsn_code": "20081920",
                "value_of_good": 0.0,
                "gst_tax_percentage": 12.0,
                "is_default_hsn_code": True,
                "brand_calculated_amount": 115.0,
                "gst_fee": "0.0"
            },
            "brand": {
                "is_virtual_invoice": False,
                "start_date": None,
                "id": 11,
                "pickup_location": None,
                "created_on": "",  # Date("2021-02-17T19:57:23.000Z"),
                "credit_note_expiry_days": None,
                "script_last_ran": None,
                "modified_on": "",  # Date("2021-02-17T19:57:23.000Z"),
                "invoice_prefix": None,
                "brand_name": "Naturoz",
                "credit_note_allowed": False,
                "logo": None,
                "company": None
            },
            "affiliate_bag_details": {
                "affiliate_bag_id": None,
                "affiliate_order_id": "16195257569000112W",
                "affiliate_meta": {
                    "fynd": {
                        "fulfilment_identifier": "infibeam"
                    }
                },
                "loyalty_discount": 0.0,
                "employee_discount": 0.0
            },
            "meta": {
                "sku": "RVSQSKQCNM",
                "name": None,
                "prices": {
                    "esp": 115,
                    "mrp": 130,
                    "meta": {},
                    "amount_paid": 115,
                    "cod_charges": 0,
                    "coupon_json": {},
                    "price_marked": 130,
                    "refund_amount": 115,
                    "promo_discount": 0,
                    "coupon_discount": 0,
                    "price_effective": 115,
                    "delivery_charges": 0,
                    "product_discount": 15,
                    "margin_percentage": 0,
                    "brand_coupon_discount": 0,
                    "brand_calculated_amount": 115
                },
                "fulfillment_type": "SMART",
                "product_category": None,
                "supporting_documents": None
            }
        }
    ],
    "requested_dp_conf": {
        "awb_type": "express",
        "exclude_dps": [],
        "ewbn": None
    },
    "restore_coupon": False,
    "rto_address": {
        "code": "7352",
        "id": 1,
        "store_address_json": {
            "area": "",
            "city": "NAVI MUMBAI",
            "email": "beinghuman.rcity@mahnada.com",
            "phone": "91000000000",
            "state": "Delhi",
            "country": "INDIA",
            "pincode": "110035",
            "version": "1.0",
            "address1": "B-57,Lawrence Road Industrial Area",
            "address2": "Near Seven Heaven Banquet Hall",
            "landmark": "",
            "latitude": 19.151343,
            "longitude": 73.009313,
            "created_at": "2020-06-29 20:34:04",
            "updated_at": "2020-06-29 20:34:04",
            "address_type": "store",
            "contact_person": "Salma",
            "address_category": "store"
        },
        "company_id": 1,
        "latitude": None,
        "longitude": None,
        "name": "Tulsi Dry Fruits",
        "location_type": "mall",
        "address1": "B-57,Lawrence Road Industrial Area",
        "address2": "Near Seven Heaven Banquet Hall",
        "city": "NAVI MUMBAI",
        "state": "Delhi",
        "country": "INDIA",
        "pincode": "110035",
        "store_email": "beinghuman.rcity@mahnada.com",
        "contact_person": "Salma",
        "phone": "91000000000"
    },
    "search_key": {
        "shipment_id": "35633J",
        "order_id": "A64C7B"
    },
    "shipment": {
        "delivery_awb_number": "503739156",
        "affiliate_shipment_id": "16195259718381635633J",
        "credit_note_id": "111250210427",
        "pdf_links": None,
        "meta": {
            "dp_id": 1,
            "weight": 0.2,
            "dimension": {
                "width": 1,
                "height": 1,
                "length": 111,
                "width_unit": "CM",
                "height_unit": "CM",
                "length_unit": "CM"
            },
            "timestamp": {
                "max": 1620476139,
                "min": 1620130539
            },
            "mixed_cart": False,
            "weight_unit": "KG",
            "ewaybill_info": None,
            "logistics_meta": {
                "dp_sort_key": "fm_priority",
                "account_info": {
                    "area_code": None,
                    "operations": "inter_city",
                    "fm_priority": 1,
                    "lm_priority": 1,
                    "payment_mode": "all",
                    "rvp_priority": 1,
                    "transport_mode": "air",
                    "assign_dp_from_sb": True,
                    "external_account_id": None,
                    "internal_account_id": "1"
                },
                "account_options": [
                    {
                        "area_code": None,
                        "operations": "inter_city",
                        "fm_priority": 1,
                        "lm_priority": 1,
                        "payment_mode": "all",
                        "rvp_priority": 1,
                        "transport_mode": "air",
                        "assign_dp_from_sb": True,
                        "external_account_id": None,
                        "internal_account_id": "1"
                    }
                ],
                "assign_dp_from_sb": True
            },
            "store_invoice_updated_date": "2021-04-27T17:46:44+00:00"
        },
        "billing_address_json": {
            "area": "",
            "city": "Thane",
            "name": "Priyanjali",
            "email": "",
            "phone": "9890682272",
            "state": "Maharashtra",
            "sector": "Thane",
            "street": "billing address",
            "flat_no": "No. 7",
            "pincode": "421303",
            "plot_no": "",
            "version": "1.0",
            "address1": " No. 7 test building name billing address Thane",
            "block_no": "",
            "floor_no": "",
            "latitude": 19.6639814,
            "tower_no": "test",
            "longitude": 73.2347815,
            "created_at": "2021-04-27 17:45:57",
            "updated_at": "2021-04-27 17:45:57",
            "address_type": "home",
            "apartment_id": None,
            "society_name": "",
            "building_name": "building name",
            "contact_person": "Priyanjali",
            "address_other_type": "",
            "billing_address_id": 335972
        },
        "vertical": "GROCERIES",
        "store_invoice_id": "JS29GY9OFWBA00018",
        "delivery_address_json": {
            "area": "",
            "city": "Thane",
            "name": "Priyanjali",
            "email": "",
            "phone": "9890682272",
            "state": "Maharashtra",
            "sector": "Thane",
            "street": "billing address",
            "flat_no": "No. 7",
            "pincode": "421303",
            "plot_no": "",
            "version": "1.0",
            "address1": " No. 7 test building name billing address Thane",
            "block_no": "",
            "floor_no": "",
            "latitude": 19.6639814,
            "tower_no": "test",
            "longitude": 73.2347815,
            "created_at": "2021-04-27T17:45:57+00:00",
            "updated_at": "2021-04-27T17:45:57+00:00",
            "address_type": "home",
            "apartment_id": None,
            "society_name": "",
            "building_name": "building name",
            "contact_person": "Priyanjali",
            "address_other_type": "",
            "delivery_address_id": None,
            "addressee_name": "Priyanjali",
            "address_category": "",
            "landmark": ""
        },
        "affiliate_id": "5ea6821b3425bb07c82a25c1",
        "parent_id": "",
        "type": "shipment",
        "fynd_order_id": "FYMP6088007D18A64C7B",
        "eway_bill_id": None,
        "tags": [],
        "id": "16195259718381635633J",
        "parent_type": None,
        "is_active": True,
        "previous_shipment_id": "16195257577191166177J",
        "created_at": "",  # Date("2021-04-27T17:49:32.000Z"),
        "packaging_type": "default"
    },
    "shipment_details": {
        "dp_id": 1
    },
    "shipment_gst": {
        "value_of_good": 0.0,
        "gst_fee": 0.0,
        "brand_calculated_amount": 115.0,
        "gstin_code": "27AAHCM2029B1ZW"
    },
    "shipment_quantity": 1,
    "shipment_status": {
        "id": 12930,
        "status": "return_accepted",
        "shipment_id": "16195259718381635633J",
        "created_at": "",  # Date("2021-04-27T17:50:36.000Z"),
        "bag_list": [
            "11250"
        ]
    },
    "shipment_status_history": [
        {
            "id": 12924,
            "status": "return_initiated",
            "shipment_id": "16195259718381635633J",
            "created_at": "2021-04-27T17:49:32+00:00",
            "bag_list": [
                "11250"
            ]
        },
        {
            "id": 12925,
            "status": "return_dp_assigned",
            "shipment_id": "16195259718381635633J",
            "created_at": "2021-04-27T17:49:33+00:00",
            "bag_list": [
                "11250"
            ]
        },
        {
            "id": 12926,
            "status": "return_bag_picked",
            "shipment_id": "16195259718381635633J",
            "created_at": "2021-04-27T17:50:15+00:00",
            "bag_list": [
                "11250"
            ]
        },
        {
            "id": 12927,
            "status": "refund_initiated",
            "shipment_id": "16195259718381635633J",
            "created_at": "2021-04-27T17:50:16+00:00",
            "bag_list": [
                "11250"
            ]
        },
        {
            "id": 12928,
            "status": "refund_acknowledged",
            "shipment_id": "16195259718381635633J",
            "created_at": "2021-04-27T17:50:16+00:00",
            "bag_list": [
                "11250"
            ]
        },
        {
            "id": 12929,
            "status": "return_bag_delivered",
            "shipment_id": "16195259718381635633J",
            "created_at": "2021-04-27T17:50:31+00:00",
            "bag_list": [
                "11250"
            ]
        },
        {
            "id": 12930,
            "status": "return_accepted",
            "shipment_id": "16195259718381635633J",
            "created_at": "2021-04-27T17:50:36+00:00",
            "bag_list": [
                "11250"
            ]
        }
    ],
    "shipment_update_time": 1619526035.73397,
    "shipment_value": 115.0,
    "tags": [],
    "total_shipment_bags": 1,
    "transaction_type": "shipment",
    "user": {
        "mongo_user_id": "1845074",
        "mobile": "9890682272",
        "id": 23,
        "gender": None,
        "last_name": "Manore",
        "email": "priyanjalimanore@gofynd.com",
        "first_name": "Priyanjali",
        "is_anonymous_user": False,
        "loyalty_card_number": None,
        "membership_id": None
    },
    "vertical": "GROCERIES",
    "weight": {
        "value": 0.2,
        "unit": "gram"
    }
}

print(create_nested_key_dictionary_mapping(d))
