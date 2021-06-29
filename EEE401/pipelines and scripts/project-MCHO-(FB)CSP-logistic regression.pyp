<?xml version='1.0' encoding='utf-8'?>
<scheme description="piipeline to be used interchangeably for CSP and FBCSP with logistic regression classifier giving output to LSL" title="project-MCHO-(FB)CSP-logistic regression" version="2.0">
	<nodes>
		<node id="0" name="Select Range" position="(-31.0, 54.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="20153ccb-7363-482f-bdcb-fd965e492020" version="1.0.0" />
		<node id="1" name="Segmentation" position="(172.0, 54.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="b50a6dad-edfa-4d80-ab13-4b534f8aae87" version="1.0.1" />
		<node id="2" name="FIR Filter" position="(71.0, 54.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter (1)" uuid="d424404d-4e63-4561-a4ab-fd563d357013" version="1.0.0" />
		<node id="3" name="Assign Target Values" position="(-136.0, 53.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Target Values" uuid="72deef85-5ba4-4c3a-94cc-60db599d644e" version="1.0.0" />
		<node id="4" name="Inject Calibration Data" position="(-220.0, 44.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owinjectcalibrationdata.OWInjectCalibrationData" title="Inject Calibration Data" uuid="edb80955-7534-4472-8a24-681c0a2f27da" version="1.0.0" />
		<node id="5" name="Import XDF" position="(-461.34000000000015, -26.620000000000005)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF (1)" uuid="01f41773-7a48-4ee3-be34-08a45c6633dc" version="1.0.0" />
		<node id="6" name="Rewrite Markers" position="(-359.0, -16.0)" project_name="NeuroPype" qualified_name="widgets.markers.owrewritemarkers.OWRewriteMarkers" title="Rewrite Markers" uuid="c27163f8-1a61-4e95-99c2-d5a76be83796" version="0.9.3" />
		<node id="7" name="Variance" position="(391.0, 91.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="b1d4a173-49eb-43fa-85dd-ddd20603e7f1" version="1.0.0" />
		<node id="8" name="Common Spatial Patterns" position="(290.0, 75.0)" project_name="NeuroPype" qualified_name="widgets.neural.owcommonspatialpatterns.OWCommonSpatialPatterns" title="Common Spatial Patterns" uuid="3573469d-8566-4966-a00d-bf43aae15a17" version="1.0.0" />
		<node id="9" name="Marker Stream Window" position="(294.0, -23.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owmarkerstreamwindow.OWMarkerStreamWindow" title="Marker Stream Window" uuid="fc8347f7-e6dd-4d8a-a38c-1f31fad8bc32" version="1.0.1" />
		<node id="10" name="Streaming Bar Plot" position="(926.0, -123.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="ea3fb131-7602-4911-8c86-b77ae8aa2213" version="1.0.2" />
		<node id="11" name="Mean" position="(775.0, -122.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owmean.OWMean" title="Mean" uuid="d5ff1bbc-1e46-4a98-ba6e-203ebed88569" version="1.0.0" />
		<node id="12" name="Logistic Regression" position="(619.0, 17.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression" uuid="a7ea5237-ee19-4378-bbdf-381b8079ccf5" version="1.0.0" />
		<node id="13" name="Logarithm" position="(519.0, 17.0)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owlogarithm.OWLogarithm" title="Logarithm" uuid="40274123-a1e2-440c-a74f-4f7775368ad0" version="1.0.0" />
		<node id="14" name="Override Axis" position="(672.0, -122.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="d5aa71d3-0e48-4297-b656-547dff60a429" version="1.0.2" />
		<node id="15" name="Time Series Plot" position="(916.0, 159.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="a8c58464-8ba1-487b-ba9f-221d84cfc226" version="1.0.1" />
		<node id="16" name="Select Range" position="(800.0, 159.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range (1)" uuid="7fc6294a-de85-4ce2-9cdd-b9bb0931f937" version="1.0.0" />
		<node id="17" name="Discard Long Chunks" position="(700.0, 159.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdiscardlongchunks.OWDiscardLongChunks" title="Discard Long Chunks" uuid="c2ddfc5d-78ea-48c5-acf8-c7e03129af87" version="1.0.0" />
		<node id="18" name="LSL Output" position="(729.0, 15.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="a9654870-bb63-47f6-abca-fd1ac4d40a01" version="1.0.0" />
		<node id="19" name="Import XDF" position="(-674.0, 105.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="aff423a0-3d41-4900-bd85-6c6b552c5a06" version="1.0.0" />
		<node id="20" name="Stream Data" position="(-383.0, 101.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="ad518d01-5f06-4fdf-8d7f-a481dea60ad3" version="1.1.0" />
		<node id="21" name="Rewrite Markers" position="(-481.0, 108.0)" project_name="NeuroPype" qualified_name="widgets.markers.owrewritemarkers.OWRewriteMarkers" title="Rewrite Markers (1)" uuid="1a3dc3c3-2223-4ce6-bc3d-aea78c84ed98" version="0.9.3" />
		<node id="22" name="Dejitter Timestamps" position="(-564.0, 106.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="6d58a203-f6d5-4670-9fc5-83b26ffc7c21" version="1.0.0" />
		<node id="23" name="Filter Bank Common Spatial Patterns" position="(-56.0, 310.0)" project_name="NeuroPype" qualified_name="widgets.neural.owfilterbankcommonspatialpattern.OWFilterBankCommonSpatialPattern" title="Filter Bank Common Spatial Patterns" uuid="d0f7a993-3a71-416f-9da4-5c4edfa74008" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="3" sink_channel="Calib Data" sink_node_id="4" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="14" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="15" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="18" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="18" sink_channel="Data" sink_node_id="20" source_channel="Data" source_node_id="21" />
		<link enabled="true" id="19" sink_channel="Data" sink_node_id="21" source_channel="Data" source_node_id="22" />
		<link enabled="true" id="20" sink_channel="Data" sink_node_id="22" source_channel="Data" source_node_id="19" />
		<link enabled="true" id="21" sink_channel="Streaming Data" sink_node_id="4" source_channel="Data" source_node_id="20" />
	</links>
	<annotations>
		<arrow end="(82.0, 130.0)" fill="#C1272D" id="0" start="(-160.0, 130.0)" />
		<arrow end="(-22.0, 300.0)" fill="#C1272D" id="1" start="(249.0, 115.0)" />
		<text font-family="Helvetica" font-size="16" id="2" rect="(77.63999999999996, 219.68000000000006, 250.0, 74.0)">to be interchanged and features generated to go through feature evaluation</text>
		<text font-family="Helvetica" font-size="16" id="3" rect="(-120.0, 126.0, 121.0, 50.0)">direction of flow</text>
	</annotations>
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGIWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAACzgAAAOoAAARFAAABtQAAAtYA
AAEJAAAEPQAAAa0AAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxYAQAAADpxDVgOAAAA
c2V0X2JyZWFrcG9pbnRxDolYBAAAAHVuaXRxD1gHAAAAaW5kaWNlc3EQdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgPAAAAb25saW5lX2Vwb2NoaW5ncQNYDQAAAG1hcmtlci1sb2NrZWRxBFgNAAAAc2FtcGxl
X29mZnNldHEFSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUK
cQdYDAAAAFB5UXQ0LlF0Q29yZXEIWAoAAABRQnl0ZUFycmF5cQlDLgHZ0MsAAQAAAAAB+wAAAMEA
AANyAAABuQAAAgMAAADgAAADagAAAbEAAAAAAABxCoVxC4dxDFJxDVgOAAAAc2VsZWN0X21hcmtl
cnNxDlgNAAAAKHVzZSBkZWZhdWx0KXEPWA4AAABzZXRfYnJlYWtwb2ludHEQiVgLAAAAdGltZV9i
b3VuZHNxEV1xEihK/////0sBZVgHAAAAdmVyYm9zZXETiXUu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsFSwhLHksgZVgNAAAAbWluaW11bV9waGFzZXEJiFgEAAAAbW9k
ZXEKWAgAAABiYW5kcGFzc3ELWAUAAABvcmRlcnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxDmNzaXAKX3VucGlja2xlX3R5cGUKcQ9YDAAAAFB5UXQ0LlF0Q29y
ZXEQWAoAAABRQnl0ZUFycmF5cRFDLgHZ0MsAAQAAAAACWAAAAXwAAAPPAAACSgAAAmAAAAGbAAAD
xwAAAkIAAAAAAABxEoVxE4dxFFJxFVgOAAAAc2V0X2JyZWFrcG9pbnRxFolYCgAAAHN0b3BfYXR0
ZW5xF0dASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYCgAAAGltYWdfZ3Jh
c3BxB0sAWAwAAABpbWFnX3JlbGVhc2VxCEsBdVgOAAAAbWFwcGluZ19mb3JtYXRxCVgGAAAAY29t
cGF0cQpYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxC2NzaXAKX3VucGlja2xlX3R5cGUKcQxYDAAA
AFB5UXQ0LlF0Q29yZXENWAoAAABRQnl0ZUFycmF5cQ5DLgHZ0MsAAQAAAAAB7wAAAQwAAANmAAAB
vwAAAfcAAAErAAADXgAAAbcAAAAAAABxD4VxEIdxEVJxElgOAAAAc2V0X2JyZWFrcG9pbnRxE4lY
EQAAAHN1cHBvcnRfd2lsZGNhcmRzcRSJWAsAAAB1c2VfbnVtYmVyc3EViVgHAAAAdmVyYm9zZXEW
iXUu
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWBcAAABkZWxheV9zdHJlYW1pbmdfcGFja2V0c3EBiVgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXECY3NpcApfdW5waWNrbGVfdHlwZQpxA1gMAAAAUHlRdDQuUXRDb3JlcQRYCgAAAFFCeXRl
QXJyYXlxBUMuAdnQywABAAAAAAHvAAABJAAAA2YAAAGnAAAB9wAAAUMAAANeAAABnwAAAAAAAHEG
hXEHh3EIUnEJWA4AAABzZXRfYnJlYWtwb2ludHEKiXUu
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWHQAAABDOi9Vc2Vycy9FbW1hbnVlbCBPbGF0ZWp1L0RvY3VtZW50cy9HaXRI
dWIvc2Nob29sIHByb2plY3RzL0VFRTQwMS9MYWIgcmVjb3JkZXIvMTAtMDUtMjAyMS9UcmFpbi9T
aW1pX1RyaWFsX1J1bl8xLnhkZnEIWBMAAABoYW5kbGVfY2xvY2tfcmVzZXRzcQmIWBEAAABoYW5k
bGVfY2xvY2tfc3luY3EKiFgVAAAAaGFuZGxlX2ppdHRlcl9yZW1vdmFscQuIWA4AAABtYXhfbWFy
a2VyX2xlbnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YEgAAAHJlb3JkZXJfdGltZXN0YW1wc3EOiVgO
AAAAcmV0YWluX3N0cmVhbXNxD2gNWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRBjc2lwCl91bnBp
Y2tsZV90eXBlCnERWAwAAABQeVF0NC5RdENvcmVxElgKAAAAUUJ5dGVBcnJheXETQy4B2dDLAAEA
AAAAAyAAAAEiAAAElwAAAiAAAAMoAAABQQAABI8AAAIYAAAAAAAAcRSFcRWHcRZScRdYDgAAAHNl
dF9icmVha3BvaW50cRiJWA8AAAB1c2Vfc3RyZWFtbmFtZXNxGYlYBwAAAHZlcmJvc2VxGol1Lg==
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAkAAABpdl9jb2x1bW5xAVgGAAAATWFya2VycQJYDgAAAHBhdHRlcm5fc3ludGF4cQNY
CQAAAHdpbGRjYXJkc3EEWAkAAAByZWdleF9zdWJxBYlYEQAAAHJlbW92ZV9hbGxfb3RoZXJzcQaJ
WAUAAABydWxlc3EHWDIAAAB7J2dyYXNwJzogJ2ltYWdfZ3Jhc3AnLCAncmVsZWFzZSc6ICdpbWFn
X3JlbGVhc2UnfXEIWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBl
CnEKWAwAAABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAAe8AAAEM
AAADZgAAAdoAAAH3AAABKwAAA14AAAHSAAAAAAAAcQ2FcQ6HcQ9ScRBYDgAAAHNldF9icmVha3Bv
aW50cRGJdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQVjc2lwCl91
bnBpY2tsZV90eXBlCnEGWAwAAABQeVF0NC5RdENvcmVxB1gKAAAAUUJ5dGVBcnJheXEIQy4B2dDL
AAEAAAAAAe8AAAEiAAADZgAAAagAAAH3AAABQQAAA14AAAGgAAAAAAAAcQmFcQqHcQtScQxYDgAA
AHNldF9icmVha3BvaW50cQ2JdS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAoAAABjb25kX2ZpZWxkcQFYCwAAAFRhcmdldFZhbHVlcQJYDwAAAGluaXRpYWxpemVf
b25jZXEDiFgDAAAAbm9mcQRLBFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNr
bGVfdHlwZQpxBlgMAAAAUHlRdDQuUXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCEMuAdnQywABAAAA
AAHvAAABIgAAA2YAAAGoAAAB9wAAAUEAAANeAAABoAAAAAAAAHEJhXEKh3ELUnEMWA4AAABzZXRf
YnJlYWtwb2ludHENiXUu
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWAwAAABpbml0aWFsX2RpbXNxAl1xAyhLMksyTfQB
TfQBZVgOAAAAb3ZlcnJpZGVfc3JhdGVxBFgNAAAAKHVzZSBkZWZhdWx0KXEFWBMAAABzYXZlZFdp
ZGdldEdlb21ldHJ5cQZjc2lwCl91bnBpY2tsZV90eXBlCnEHWAwAAABQeVF0NC5RdENvcmVxCFgK
AAAAUUJ5dGVBcnJheXEJQy4B2dDLAAEAAAAAAe8AAAEYAAADZgAAAbMAAAH3AAABNwAAA14AAAGr
AAAAAAAAcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAsAAABzdHJlYW1fbmFtZXEP
WAcAAABNYXJrZXJzcRB1Lg==
</properties>
		<properties format="literal" node_id="10">{'always_on_top': False, 'axis': 'feature', 'background_color': '#FFFFFF', 'bar_color': 'b', 'bar_width': 0.9, 'initial_dims': [800, 50, 700, 500], 'instance_field': '(use default)', 'label_rotation': 'horizontal', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'show_toolbar': False, 'stream_name': '(use default)', 'title': 'Classification', 'use_last_instance': True, 'verbose': False, 'y_limits': [0, 1]}</properties>
		<properties format="literal" node_id="11">{'axis': 'instance', 'force_feature_axis': False, 'ignore_nans': False, 'robust': False, 'robust_estimator_type': 'median', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'trim_proportion': 0.1}</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYBAAA
AGF1dG9xBVgKAAAAY29uZF9maWVsZHEGWAsAAABUYXJnZXRWYWx1ZXEHWBAAAABkb250X3Jlc2V0
X21vZGVscQiJWBAAAABkdWFsX2Zvcm11bGF0aW9ucQmJWAwAAABpbmNsdWRlX2JpYXNxCohYDwAA
AGluaXRpYWxpemVfb25jZXELiFgIAAAAbWF4X2l0ZXJxDEtkWAoAAABtdWx0aWNsYXNzcQ1YAwAA
AG92cnEOWAkAAABudW1fZm9sZHNxD0sFWAgAAABudW1fam9ic3EQSwFYDQAAAHByb2JhYmlsaXN0
aWNxEYhYCwAAAHJlZ3VsYXJpemVycRJYAgAAAGwycRNYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlx
FGNzaXAKX3VucGlja2xlX3R5cGUKcRVYDAAAAFB5UXQ0LlF0Q29yZXEWWAoAAABRQnl0ZUFycmF5
cRdDLgHZ0MsAAQAAAAAB7wAAAPQAAANmAAAB1wAAAfcAAAETAAADXgAAAc8AAAAAAABxGIVxGYdx
GlJxG1gNAAAAc2VhcmNoX21ldHJpY3EcWAgAAABhY2N1cmFjeXEdWA4AAABzZXRfYnJlYWtwb2lu
dHEeiVgGAAAAc29sdmVycR9YBQAAAGxiZmdzcSBYCQAAAHRvbGVyYW5jZXEhRz8aNuLrHEMtWAkA
AAB2ZXJib3NpdHlxIksAdS4=
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAQAAABiYXNlcQFYDQAAACh1c2UgZGVmYXVsdClxAlgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXEDY3NpcApfdW5waWNrbGVfdHlwZQpxBFgMAAAAUHlRdDQuUXRDb3JlcQVYCgAAAFFCeXRl
QXJyYXlxBkMuAdnQywABAAAAAAHvAAABIgAAA2YAAAGoAAAB9wAAAUEAAANeAAABoAAAAAAAAHEH
hXEIh3EJUnEKWA4AAABzZXRfYnJlYWtwb2ludHELiXUu
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4lYDAAAAGN1c3RvbV9sYWJlbHEEWA0AAAAodXNlIGRlZmF1
bHQpcQVYCQAAAGluaXRfZGF0YXEGXXEHKFgEAAAAbGVmdHEIWAUAAAByaWdodHEJZVgIAAAAbmV3
X2F4aXNxClgHAAAAZmVhdHVyZXELWAgAAABvbGRfYXhpc3EMWAcAAABmZWF0dXJlcQ1YDAAAAG9u
bHlfc2lnbmFsc3EOiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEPY3NpcApfdW5waWNrbGVfdHlw
ZQpxEFgMAAAAUHlRdDQuUXRDb3JlcRFYCgAAAFFCeXRlQXJyYXlxEkMuAdnQywABAAAAAAHvAAAA
6QAAA2YAAAHhAAAB9wAAAQgAAANeAAAB2QAAAAAAAHEThXEUh3EVUnEWWA4AAABzZXRfYnJlYWtw
b2ludHEXiXUu
</properties>
		<properties format="literal" node_id="15">{'absolute_time': False, 'always_on_top': False, 'antialiased': True, 'auto_line_colors': False, 'autoscale': False, 'background_color': '#FFFFFF', 'decoration_color': '#000000', 'downsampled': False, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'line_width': 0.75, 'marker_color': {'*': '#FFFFFF', 'left': '#FF0000', 'right': '#00FF00'}, 'nans_as_zero': False, 'no_concatenate': False, 'override_srate': '(use default)', 'plot_markers': True, 'plot_minmax': False, 'savedWidgetGeometry': None, 'scale': 1.0, 'set_breakpoint': False, 'show_toolbar': False, 'stream_name': '(use default)', 'time_range': 30.0, 'title': 'Time series view', 'zero_color': '#7F7F7F', 'zeromean': False}</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVx
A1gTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlR
dDQuUXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0MuAdnQywABAAAAAAHvAAABAAAAA2YAAAHLAAAB
9wAAAR8AAANeAAABwwAAAAAAAHEIhXEJh3EKUnELWAkAAABzZWxlY3Rpb25xDF1xDUsAYVgOAAAA
c2V0X2JyZWFrcG9pbnRxDolYBAAAAHVuaXRxD1gHAAAAaW5kaWNlc3EQdS4=
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWA0AAABlbnRpcmVfcGFja2V0cQGIWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQJjc2lw
Cl91bnBpY2tsZV90eXBlCnEDWAwAAABQeVF0NC5RdENvcmVxBFgKAAAAUUJ5dGVBcnJheXEFQy4B
2dDLAAEAAAAAAe8AAAEYAAADZgAAAbMAAAH3AAABNwAAA14AAAGrAAAAAAAAcQaFcQeHcQhScQlY
DgAAAHNldF9icmVha3BvaW50cQqJWAkAAAB0aHJlc2hvbGRxC0sKdS4=
</properties>
		<properties format="pickle" node_id="18">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYFgAAAFBDQS10ZXN0U3RyZWFtLU1hcmtlcnNxBFgQAAAAbWFya2VyX3Nv
dXJjZV9pZHEFWAAAAABxBlgMAAAAbWF4X2J1ZmZlcmVkcQdLPFgXAAAAcmVzZXRfaWZfbGFiZWxz
X2NoYW5nZWRxCIlYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCWNzaXAKX3VucGlja2xlX3R5cGUK
cQpYDAAAAFB5UXQ0LlF0Q29yZXELWAoAAABRQnl0ZUFycmF5cQxDLgHZ0MsAAQAAAAAB7wAAAKYA
AANmAAACJQAAAfcAAADFAAADXgAAAh0AAAAAAABxDYVxDodxD1JxEFgMAAAAc2VuZF9tYXJrZXJz
cRGJWA4AAABzZXRfYnJlYWtwb2ludHESiVgJAAAAc291cmNlX2lkcRNYKgAAAChuZXZlciB1c2Ug
c2FtZSBzb3VyY2UgaWQgaW4gb25lIHB5cGVsaW5lKXEUWAUAAABzcmF0ZXEVWA0AAAAodXNlIGRl
ZmF1bHQpcRZYCwAAAHN0cmVhbV9uYW1lcRdYDgAAAFBDQS10ZXN0U3RyZWFtcRhYCwAAAHN0cmVh
bV90eXBlcRlYAwAAAEVFR3EaWBMAAAB1c2VfZGF0YV90aW1lc3RhbXBzcRuIWBYAAAB1c2VfbnVt
cHlfb3B0aW1pemF0aW9ucRyJdS4=
</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWG0AAABDOi9Vc2Vycy9FbW1hbnVlbCBPbGF0ZWp1L0RvY3VtZW50cy9HaXRI
dWIvc2Nob29sIHByb2plY3RzL0VFRTQwMS9MYWIgcmVjb3JkZXIvMTAtMDUtMjAyMS9UZXN0L1Np
bWlfUnVuXzEueGRmcQhYEwAAAGhhbmRsZV9jbG9ja19yZXNldHNxCYhYEQAAAGhhbmRsZV9jbG9j
a19zeW5jcQqIWBUAAABoYW5kbGVfaml0dGVyX3JlbW92YWxxC4hYDgAAAG1heF9tYXJrZXJfbGVu
cQxYDQAAACh1c2UgZGVmYXVsdClxDVgSAAAAcmVvcmRlcl90aW1lc3RhbXBzcQ6JWA4AAAByZXRh
aW5fc3RyZWFtc3EPaA1YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlja2xlX3R5
cGUKcRFYDAAAAFB5UXQ0LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDLgHZ0MsAAQAAAAAD3gAA
ARAAAAVVAAACJAAAA+YAAAEvAAAFTQAAAhwAAAAAAABxFIVxFYdxFlJxF1gOAAAAc2V0X2JyZWFr
cG9pbnRxGIlYDwAAAHVzZV9zdHJlYW1uYW1lc3EZiVgHAAAAdmVyYm9zZXEaiXUu
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWBEAAABoaXRjaF9wcm9iYWJpbGl0eXEBRwAAAAAAAAAAWA4AAABqaXR0ZXJfcGVyY2Vu
dHECSwVYBwAAAGxvb3BpbmdxA4hYCAAAAHJhbmRzZWVkcQRN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBWNzaXAKX3VucGlja2xlX3R5cGUKcQZYDAAAAFB5UXQ0LlF0Q29yZXEHWAoAAABRQnl0
ZUFycmF5cQhDLgHZ0MsAAQAAAAAB7wAAANAAAANmAAACKwAAAfcAAADvAAADXgAAAiMAAAAAAABx
CYVxCodxC1JxDFgOAAAAc2V0X2JyZWFrcG9pbnRxDYlYBwAAAHNwZWVkdXBxDkc/8AAAAAAAAFgJ
AAAAc3RhcnRfcG9zcQ9HAAAAAAAAAABYEAAAAHRpbWVzdGFtcF9qaXR0ZXJxEEcAAAAAAAAAAFgG
AAAAdGltaW5ncRFYDQAAAGRldGVybWluaXN0aWNxElgPAAAAdXBkYXRlX2ludGVydmFscRNHP6R6
4UeuFHt1Lg==
</properties>
		<properties format="pickle" node_id="21">gAN9cQAoWAkAAABpdl9jb2x1bW5xAVgGAAAATWFya2VycQJYDgAAAHBhdHRlcm5fc3ludGF4cQNY
CQAAAHdpbGRjYXJkc3EEWAkAAAByZWdleF9zdWJxBYlYEQAAAHJlbW92ZV9hbGxfb3RoZXJzcQaJ
WAUAAABydWxlc3EHWDIAAAB7J2dyYXNwJzogJ2ltYWctZ3Jhc3AnLCAncmVsZWFzZSc6ICdpbWFn
X3JlbGVhc2UnfXEIWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBl
CnEKWAwAAABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAAe8AAAEM
AAADZgAAAb8AAAH3AAABKwAAA14AAAG3AAAAAAAAcQ2FcQ6HcQ9ScRBYDgAAAHNldF9icmVha3Bv
aW50cRGJdS4=
</properties>
		<properties format="pickle" node_id="22">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlj
a2xlX3R5cGUKcQVYDAAAAFB5UXQ0LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAA
AAAB7wAAAS4AAANmAAABnAAAAfcAAAFNAAADXgAAAZQAAAAAAABxCIVxCYdxClJxC1gOAAAAc2V0
X2JyZWFrcG9pbnRxDIlYDgAAAHdhcm11cF9zYW1wbGVzcQ1K/////3Uu
</properties>
		<properties format="literal" node_id="23">{'bands': [[0.5, 3], [4, 7], [8, 12], [13, 30], [31, 42]], 'cond_field': 'TargetValue', 'initialize_once': True, 'min_fft_size': 256, 'nof': 3, 'overlap_length': '(use default)', 'overlap_unit': 'samples', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'shrinkage': 0, 'window_func': 'hann', 'window_length': '(use default)', 'window_param': '(use default)', 'window_unit': 'samples'}</properties>
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
            "node3",
            "data",
            "node2",
            "data"
        ],
        [
            "node4",
            "data",
            "node1",
            "data"
        ],
        [
            "node5",
            "data",
            "node4",
            "data"
        ],
        [
            "node7",
            "data",
            "node5",
            "calib_data"
        ],
        [
            "node6",
            "data",
            "node7",
            "data"
        ],
        [
            "node1",
            "data",
            "node3",
            "data"
        ],
        [
            "node2",
            "data",
            "node10",
            "data"
        ],
        [
            "node2",
            "data",
            "node9",
            "data"
        ],
        [
            "node9",
            "data",
            "node8",
            "data"
        ],
        [
            "node12",
            "data",
            "node11",
            "data"
        ],
        [
            "node15",
            "data",
            "node12",
            "data"
        ],
        [
            "node14",
            "data",
            "node13",
            "data"
        ],
        [
            "node13",
            "data",
            "node15",
            "data"
        ],
        [
            "node13",
            "data",
            "node18",
            "data"
        ],
        [
            "node13",
            "data",
            "node19",
            "data"
        ],
        [
            "node8",
            "data",
            "node14",
            "data"
        ],
        [
            "node18",
            "data",
            "node17",
            "data"
        ],
        [
            "node17",
            "data",
            "node16",
            "data"
        ],
        [
            "node22",
            "data",
            "node21",
            "data"
        ],
        [
            "node23",
            "data",
            "node22",
            "data"
        ],
        [
            "node20",
            "data",
            "node23",
            "data"
        ],
        [
            "node21",
            "data",
            "node5",
            "streaming_data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
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
            "uuid": "20153ccb-7363-482f-bdcb-fd965e492020"
        },
        "node10": {
            "class": "MarkerStreamWindow",
            "module": "neuropype.nodes.visualization.MarkerStreamWindow",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        500,
                        500
                    ]
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Markers"
                }
            },
            "uuid": "fc8347f7-e6dd-4d8a-a38c-1f31fad8bc32"
        },
        "node11": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.9
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        800,
                        50,
                        700,
                        500
                    ]
                },
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "horizontal"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Classification"
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "y_limits": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                }
            },
            "uuid": "ea3fb131-7602-4911-8c86-b77ae8aa2213"
        },
        "node12": {
            "class": "Mean",
            "module": "neuropype.nodes.statistics.Mean",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "instance"
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust_estimator_type": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "median"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "trim_proportion": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                }
            },
            "uuid": "d5ff1bbc-1e46-4a98-ba6e-203ebed88569"
        },
        "node13": {
            "class": "LogisticRegression",
            "module": "neuropype.nodes.machine_learning.LogisticRegression",
            "params": {
                "alphas": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        1.0,
                        5,
                        10.0
                    ]
                },
                "bias_scaling": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "class_weights": {
                    "customized": true,
                    "type": "Port",
                    "value": "auto"
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "dual_formulation": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "include_bias": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_iter": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "multiclass": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "ovr"
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "num_jobs": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "regularizer": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "l2"
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "lbfgs"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "a7ea5237-ee19-4378-bbdf-381b8079ccf5"
        },
        "node14": {
            "class": "Logarithm",
            "module": "neuropype.nodes.elementwise_math.Logarithm",
            "params": {
                "base": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "40274123-a1e2-440c-a74f-4f7775368ad0"
        },
        "node15": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "left",
                        "right"
                    ]
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "d5aa71d3-0e48-4297-b656-547dff60a429"
        },
        "node16": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "*": "#FFFFFF",
                        "left": "#FF0000",
                        "right": "#00FF00"
                    }
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 30.0
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Time series view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "a8c58464-8ba1-487b-ba9f-221d84cfc226"
        },
        "node17": {
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
                    "value": "feature"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        0
                    ]
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
            "uuid": "7fc6294a-de85-4ce2-9cdd-b9bb0931f937"
        },
        "node18": {
            "class": "DiscardLongChunks",
            "module": "neuropype.nodes.utilities.DiscardLongChunks",
            "params": {
                "entire_packet": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "threshold": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 10
                }
            },
            "uuid": "c2ddfc5d-78ea-48c5-acf8-c7e03129af87"
        },
        "node19": {
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
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
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
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "(never use same source id in one pypeline)"
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
            "uuid": "a9654870-bb63-47f6-abca-fd1ac4d40a01"
        },
        "node2": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "max_gap_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "online_epoching": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "marker-locked"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        -1,
                        1
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "b50a6dad-edfa-4d80-ab13-4b534f8aae87"
        },
        "node20": {
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
                    "value": "C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Lab recorder/10-05-2021/Test/Simi_Run_1.xdf"
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
            "uuid": "aff423a0-3d41-4900-bd85-6c6b552c5a06"
        },
        "node21": {
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
            "uuid": "ad518d01-5f06-4fdf-8d7f-a481dea60ad3"
        },
        "node22": {
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
                    "value": "{'grasp': 'imag-grasp', 'release': 'imag_release'}"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "1a3dc3c3-2223-4ce6-bc3d-aea78c84ed98"
        },
        "node23": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "6d58a203-f6d5-4670-9fc5-83b26ffc7c21"
        },
        "node24": {
            "class": "FilterBankCommonSpatialPattern",
            "module": "neuropype.nodes.neural.FilterBankCommonSpatialPattern",
            "params": {
                "bands": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        [
                            0.5,
                            3
                        ],
                        [
                            4,
                            7
                        ],
                        [
                            8,
                            12
                        ],
                        [
                            13,
                            30
                        ],
                        [
                            31,
                            42
                        ]
                    ]
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "min_fft_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 256
                },
                "nof": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "overlap_length": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "overlap_unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "samples"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0
                },
                "window_func": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "hann"
                },
                "window_length": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "window_param": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "window_unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "samples"
                }
            },
            "uuid": "d0f7a993-3a71-416f-9da4-5c4edfa74008"
        },
        "node3": {
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
            "uuid": "d424404d-4e63-4561-a4ab-fd563d357013"
        },
        "node4": {
            "class": "AssignTargets",
            "module": "neuropype.nodes.machine_learning.AssignTargets",
            "params": {
                "also_legacy_output": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "is_categorical": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "mapping": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "imag_grasp": 0,
                        "imag_release": 1
                    }
                },
                "mapping_format": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "compat"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numbers": {
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
            "uuid": "72deef85-5ba4-4c3a-94cc-60db599d644e"
        },
        "node5": {
            "class": "InjectCalibrationData",
            "module": "neuropype.nodes.machine_learning.InjectCalibrationData",
            "params": {
                "delay_streaming_packets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "edb80955-7534-4472-8a24-681c0a2f27da"
        },
        "node6": {
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
                    "value": "C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Lab recorder/10-05-2021/Train/Simi_Trial_Run_1.xdf"
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
            "uuid": "01f41773-7a48-4ee3-be34-08a45c6633dc"
        },
        "node7": {
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
            "uuid": "c27163f8-1a61-4e95-99c2-d5a76be83796"
        },
        "node8": {
            "class": "Variance",
            "module": "neuropype.nodes.statistics.Variance",
            "params": {
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "time"
                },
                "degrees_of_freedom": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "b1d4a173-49eb-43fa-85dd-ddd20603e7f1"
        },
        "node9": {
            "class": "CommonSpatialPatterns",
            "module": "neuropype.nodes.neural.CommonSpatialPatterns",
            "params": {
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "nof": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 4
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "3573469d-8566-4966-a00d-bf43aae15a17"
        }
    },
    "version": 1.1
}</patch>
</scheme>
