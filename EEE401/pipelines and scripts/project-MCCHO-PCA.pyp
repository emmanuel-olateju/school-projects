<?xml version='1.0' encoding='utf-8'?>
<scheme description="The project MCCHO using principal component analysis as our features extraction method" title="project-MCCHO-PCA" version="2.0">
	<nodes>
		<node id="0" name="Select Range" position="(306.0, 174.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="f2bbc058-2d2d-4935-9942-440b78415343" version="1.0.0" />
		<node id="1" name="FIR Filter" position="(406.0, 174.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="4ae52bd8-f875-4709-af48-937452a6a9c1" version="1.0.0" />
		<node id="2" name="Stream Data" position="(200.0, 173.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="8fe6440e-3f8a-4507-b2d5-5c5312cd28f5" version="1.1.0" />
		<node id="3" name="Override Axis" position="(509.0, 173.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="7b6284cf-537d-4eaf-83dd-e2ea454fb020" version="1.0.2" />
		<node id="4" name="Import XDF" position="(22.0, 171.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF (1)" uuid="8659c2e3-5b1b-41bc-a183-b106995e2baf" version="1.0.0" />
		<node id="5" name="Rewrite Markers" position="(111.0, 173.0)" project_name="NeuroPype" qualified_name="widgets.markers.owrewritemarkers.OWRewriteMarkers" title="Rewrite Markers (1)" uuid="c5aece41-fb50-4a27-bac6-286930c80858" version="0.9.3" />
		<node id="6" name="LSL Output" position="(598.0, 173.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="a559d24d-aa14-47f0-b95f-3804b2f1968c" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="1" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAD3gAAAQAAAAVVAAABywAAA+YA
AAEfAAAFTQAAAcMAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxYAQAAADpxDVgOAAAA
c2V0X2JyZWFrcG9pbnRxDolYBAAAAHVuaXRxD1gHAAAAaW5kaWNlc3EQdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsFSwhLHksgZVgNAAAAbWluaW11bV9waGFzZXEJiFgEAAAAbW9k
ZXEKWAgAAABiYW5kcGFzc3ELWAUAAABvcmRlcnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxDmNzaXAKX3VucGlja2xlX3R5cGUKcQ9YDAAAAFB5UXQ0LlF0Q29y
ZXEQWAoAAABRQnl0ZUFycmF5cRFDLgHZ0MsAAQAAAAAD3gAAAQwAAAVVAAABvwAAA+YAAAErAAAF
TQAAAbcAAAAAAABxEoVxE4dxFFJxFVgOAAAAc2V0X2JyZWFrcG9pbnRxFolYCgAAAHN0b3BfYXR0
ZW5xF0dASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWBEAAABoaXRjaF9wcm9iYWJpbGl0eXEBRwAAAAAAAAAAWA4AAABqaXR0ZXJfcGVyY2Vu
dHECSwVYBwAAAGxvb3BpbmdxA4hYCAAAAHJhbmRzZWVkcQRN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBWNzaXAKX3VucGlja2xlX3R5cGUKcQZYDAAAAFB5UXQ0LlF0Q29yZXEHWAoAAABRQnl0
ZUFycmF5cQhDLgHZ0MsAAQAAAAACeAAAAO4AAAPvAAACNAAAAoAAAAENAAAD5wAAAiwAAAAAAABx
CYVxCodxC1JxDFgOAAAAc2V0X2JyZWFrcG9pbnRxDYlYBwAAAHNwZWVkdXBxDkc/8AAAAAAAAFgJ
AAAAc3RhcnRfcG9zcQ9HAAAAAAAAAABYEAAAAHRpbWVzdGFtcF9qaXR0ZXJxEEcAAAAAAAAAAFgG
AAAAdGltaW5ncRFYDQAAAGRldGVybWluaXN0aWNxElgPAAAAdXBkYXRlX2ludGVydmFscRNHP6R6
4UeuFHt1Lg==
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKJWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4hYDAAAAGN1c3RvbV9sYWJlbHEEWAoAAAAnY2hhbm5lbHMn
cQVYCQAAAGluaXRfZGF0YXEGXXEHKFgDAAAARnAxcQhYAwAAAEZwMnEJWAIAAABDM3EKWAIAAABD
NHELWAIAAABQN3EMWAIAAABQOHENWAIAAABPMXEOWAIAAABPMnEPZVgIAAAAbmV3X2F4aXNxEFgF
AAAAc3BhY2VxEVgIAAAAb2xkX2F4aXNxElgFAAAAc3BhY2VxE1gMAAAAb25seV9zaWduYWxzcRSI
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRVjc2lwCl91bnBpY2tsZV90eXBlCnEWWAwAAABQeVF0
NC5RdENvcmVxF1gKAAAAUUJ5dGVBcnJheXEYQy4B2dDLAAEAAAAAAlwAAADGAAAD0wAAAb4AAAJk
AAAA5QAAA8sAAAG2AAAAAAAAcRmFcRqHcRtScRxYDgAAAHNldF9icmVha3BvaW50cR2JdS4=
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWG8AAABDOi9Vc2Vycy9FbW1hbnVlbCBPbGF0ZWp1L0RvY3VtZW50cy9HaXRI
dWIvc2Nob29sIHByb2plY3RzL0VFRTQwMS9MYWIgcmVjb3JkZXIvMTAtMDUtMjAyMS9UZXN0L1Nh
bXNvbl9SdW5fMS54ZGZxCFgTAAAAaGFuZGxlX2Nsb2NrX3Jlc2V0c3EJiFgRAAAAaGFuZGxlX2Ns
b2NrX3N5bmNxCohYFQAAAGhhbmRsZV9qaXR0ZXJfcmVtb3ZhbHELiFgOAAAAbWF4X21hcmtlcl9s
ZW5xDFgNAAAAKHVzZSBkZWZhdWx0KXENWBIAAAByZW9yZGVyX3RpbWVzdGFtcHNxDolYDgAAAHJl
dGFpbl9zdHJlYW1zcQ9oDVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEQY3NpcApfdW5waWNrbGVf
dHlwZQpxEVgMAAAAUHlRdDQuUXRDb3JlcRJYCgAAAFFCeXRlQXJyYXlxE0MuAdnQywABAAAAAAH7
AAAAtwAAA3IAAAG1AAACAwAAANYAAANqAAABrQAAAAAAAHEUhXEVh3EWUnEXWA4AAABzZXRfYnJl
YWtwb2ludHEYiVgPAAAAdXNlX3N0cmVhbW5hbWVzcRmJWAcAAAB2ZXJib3NlcRqJdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAkAAABpdl9jb2x1bW5xAVgGAAAATWFya2VycQJYDgAAAHBhdHRlcm5fc3ludGF4cQNY
CQAAAHdpbGRjYXJkc3EEWAkAAAByZWdleF9zdWJxBYlYEQAAAHJlbW92ZV9hbGxfb3RoZXJzcQaJ
WAUAAABydWxlc3EHWDIAAAB7J2dyYXNwJzogJ2ltYWdfZ3Jhc3AnLCAncmVsZWFzZSc6ICdpbWFn
X3JlbGVhc2UnfXEIWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBl
CnEKWAwAAABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAAe8AAAEM
AAADZgAAAb8AAAH3AAABKwAAA14AAAG3AAAAAAAAcQ2FcQ6HcQ9ScRBYDgAAAHNldF9icmVha3Bv
aW50cRGJdS4=
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYFgAAAFBDQS10ZXN0U3RyZWFtLU1hcmtlcnNxBFgQAAAAbWFya2VyX3Nv
dXJjZV9pZHEFWA8AAABQQ0EtdGVzdE1hcmtlcnNxBlgMAAAAbWF4X2J1ZmZlcmVkcQdLPFgXAAAA
cmVzZXRfaWZfbGFiZWxzX2NoYW5nZWRxCIlYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCWNzaXAK
X3VucGlja2xlX3R5cGUKcQpYDAAAAFB5UXQ0LlF0Q29yZXELWAoAAABRQnl0ZUFycmF5cQxDLgHZ
0MsAAQAA///+dgAAAFL////tAAAB0f///n4AAABx////5QAAAckAAAABAABxDYVxDodxD1JxEFgM
AAAAc2VuZF9tYXJrZXJzcRGIWA4AAABzZXRfYnJlYWtwb2ludHESiVgJAAAAc291cmNlX2lkcRNY
CAAAAFBDQS10ZXN0cRRYBQAAAHNyYXRlcRVYDQAAACh1c2UgZGVmYXVsdClxFlgLAAAAc3RyZWFt
X25hbWVxF1gOAAAAUENBLXRlc3RTdHJlYW1xGFgLAAAAc3RyZWFtX3R5cGVxGVgDAAAARUVHcRpY
EwAAAHVzZV9kYXRhX3RpbWVzdGFtcHNxG4hYFgAAAHVzZV9udW1weV9vcHRpbWl6YXRpb25xHIl1
Lg==
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node1",
            "data",
            "node2",
            "data"
        ],
        [
            "node3",
            "data",
            "node1",
            "data"
        ],
        [
            "node5",
            "data",
            "node6",
            "data"
        ],
        [
            "node6",
            "data",
            "node3",
            "data"
        ],
        [
            "node4",
            "data",
            "node7",
            "data"
        ],
        [
            "node2",
            "data",
            "node4",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "selection": {
                    "customized": false,
                    "type": "Port",
                    "value": ":"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "f2bbc058-2d2d-4935-9942-440b78415343"
        },
        "node2": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        5,
                        8,
                        30,
                        32
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "4ae52bd8-f875-4709-af48-937452a6a9c1"
        },
        "node3": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "looping": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "deterministic"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "8fe6440e-3f8a-4507-b2d5-5c5312cd28f5"
        },
        "node4": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "carry_over_numbers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "custom_label": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "'channels'"
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Fp1",
                        "Fp2",
                        "C3",
                        "C4",
                        "P7",
                        "P8",
                        "O1",
                        "O2"
                    ]
                },
                "new_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "old_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "only_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "7b6284cf-537d-4eaf-83dd-e2ea454fb020"
        },
        "node5": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Lab recorder/10-05-2021/Test/Samson_Run_1.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "8659c2e3-5b1b-41bc-a183-b106995e2baf"
        },
        "node6": {
            "class": "RewriteMarkers",
            "module": "neuropype.nodes.markers.RewriteMarkers",
            "params": {
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "pattern_syntax": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wildcards"
                },
                "regex_sub": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "remove_all_others": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "rules": {
                    "customized": true,
                    "type": "Port",
                    "value": "{'grasp': 'imag_grasp', 'release': 'imag_release'}"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "c5aece41-fb50-4a27-bac6-286930c80858"
        },
        "node7": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "PCA-testStream-Markers"
                },
                "marker_source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "PCA-testMarkers"
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "PCA-test"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "PCA-testStream"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "a559d24d-aa14-47f0-b95f-3804b2f1968c"
        }
    },
    "version": 1.1
}</patch>
</scheme>
