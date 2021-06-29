<?xml version='1.0' encoding='utf-8'?>
<scheme description="pipeline to be used interhangeably for (FB)CSP extraction of train and est dataset features" title="project-MCHO-(FB)CSP-offline" version="2.0">
	<nodes>
		<node id="0" name="Stream Data" position="(-401.0, 275.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="236e3f70-e4be-48b1-a0bc-5c5487e351cf" version="1.1.0" />
		<node id="1" name="Select Range" position="(-31.0, 54.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="8b291910-9ac0-42d1-a217-60f640e8ca43" version="1.0.0" />
		<node id="2" name="Segmentation" position="(172.0, 54.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="7505aa50-077b-47bd-85f6-e993f1332e94" version="1.0.1" />
		<node id="3" name="FIR Filter" position="(71.0, 54.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter (1)" uuid="e41c19aa-03bf-4c31-83ea-997af96e28c7" version="1.0.0" />
		<node id="4" name="Assign Target Values" position="(-136.0, 53.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Target Values" uuid="7bc99b22-f47a-4557-afbe-d8a92b0d7def" version="1.0.0" />
		<node id="5" name="Inject Calibration Data" position="(-220.0, 44.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owinjectcalibrationdata.OWInjectCalibrationData" title="Inject Calibration Data" uuid="d6de3ed8-62d6-4d5c-a598-15caed206612" version="1.0.0" />
		<node id="6" name="Import XDF" position="(-692.0, 279.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="12ec016e-cf7c-4772-a39d-67db44ebf90b" version="1.0.0" />
		<node id="7" name="Import XDF" position="(-461.34000000000015, -26.620000000000005)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF (1)" uuid="2a448767-54c7-4013-80af-951b2ee20a31" version="1.0.0" />
		<node id="8" name="Rewrite Markers" position="(-359.0, -16.0)" project_name="NeuroPype" qualified_name="widgets.markers.owrewritemarkers.OWRewriteMarkers" title="Rewrite Markers" uuid="9c4d3bc3-8ce2-4f4a-a43f-800d02fe24f5" version="0.9.3" />
		<node id="9" name="Rewrite Markers" position="(-499.0, 282.0)" project_name="NeuroPype" qualified_name="widgets.markers.owrewritemarkers.OWRewriteMarkers" title="Rewrite Markers (1)" uuid="a4197cb1-6a67-48de-831f-1c4809bde65c" version="0.9.3" />
		<node id="10" name="Variance" position="(391.0, 91.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="adaa55f2-0498-4ccb-bed6-748acc01c404" version="1.0.0" />
		<node id="11" name="Filter Bank Common Spatial Patterns" position="(271.0, 93.0)" project_name="NeuroPype" qualified_name="widgets.neural.owfilterbankcommonspatialpattern.OWFilterBankCommonSpatialPattern" title="Filter Bank Common Spatial Patterns" uuid="7b7c80ea-4c68-47ef-b526-dd8aad4542b1" version="1.0.0" />
		<node id="12" name="Common Spatial Patterns" position="(-58.0, 304.0)" project_name="NeuroPype" qualified_name="widgets.neural.owcommonspatialpatterns.OWCommonSpatialPatterns" title="Common Spatial Patterns" uuid="9062a10e-268e-422e-ba5d-8eb8d18ea3df" version="1.0.0" />
		<node id="13" name="Record to CSV" position="(584.0, 91.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" title="Record to CSV (1)" uuid="375d7981-9967-4b19-ba42-42b593f8e3ce" version="1.0.0" />
		<node id="14" name="Export Markers to CSV" position="(-350.0, -123.0)" project_name="NeuroPype" qualified_name="widgets.markers.owexportmarkers.OWExportMarkers" title="Export Markers to CSV (1)" uuid="a23e5a45-3ea1-40d1-a69d-b206533135b5" version="1.0.0" />
		<node id="15" name="Marker Stream Window" position="(294.0, -23.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owmarkerstreamwindow.OWMarkerStreamWindow" title="Marker Stream Window" uuid="102e9449-caad-4631-b88e-956f26e4c068" version="1.0.1" />
		<node id="16" name="Export Markers to CSV" position="(-389.0, 377.0)" project_name="NeuroPype" qualified_name="widgets.markers.owexportmarkers.OWExportMarkers" title="Export Markers to CSV" uuid="164cf91b-331a-47cd-b87e-9622b8def7da" version="1.0.0" />
		<node id="17" name="LSL Output" position="(-298.0200000000001, 271.02)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="7478375d-0518-4cf6-8c20-585dffd8d11f" version="1.0.0" />
		<node id="18" name="LSL Input" position="(-494.0, 120.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="b09d5f61-5773-49ac-b125-4868e6dd60ae" version="1.0.0" />
		<node id="19" name="Dejitter Timestamps" position="(-582.0, 280.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="71323f30-d8fe-4ea4-9240-24334e7a7c1a" version="1.0.0" />
		<node id="20" name="Override Axis" position="(483.0, 91.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis (1)" uuid="0036700c-828c-40f4-b062-d4eebd5ee55b" version="1.0.2" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="3" sink_channel="Calib Data" sink_node_id="5" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="19" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="19" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="20" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="15" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="20" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="7" />
	</links>
	<annotations>
		<arrow end="(82.0, 130.0)" fill="#C1272D" id="0" start="(-160.0, 130.0)" />
		<arrow end="(-22.0, 300.0)" fill="#C1272D" id="1" start="(249.0, 115.0)" />
		<text font-family="Helvetica" font-size="16" id="2" rect="(77.63999999999996, 219.68000000000006, 250.0, 74.0)">to be interchanged and features generated to go through feature evaluation</text>
		<text font-family="Helvetica" font-size="16" id="3" rect="(-415.0, 120.0, 221.0, 59.0)">link after extracting training features and markers</text>
		<text font-family="Helvetica" font-size="16" id="4" rect="(-120.0, 126.0, 121.0, 50.0)">direction of flow</text>
		<arrow end="(-263.0, 86.0)" fill="#C1272D" id="5" start="(-458.0, 135.0)" />
	</annotations>
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBEAAABoaXRjaF9wcm9iYWJpbGl0eXEBRwAAAAAAAAAAWA4AAABqaXR0ZXJfcGVyY2Vu
dHECSwVYBwAAAGxvb3BpbmdxA4hYCAAAAHJhbmRzZWVkcQRN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBWNzaXAKX3VucGlja2xlX3R5cGUKcQZYDAAAAFB5UXQ0LlF0Q29yZXEHWAoAAABRQnl0
ZUFycmF5cQhDLgHZ0MsAAQAAAAAB7wAAANAAAANmAAACKwAAAfcAAADvAAADXgAAAiMAAAAAAABx
CYVxCodxC1JxDFgOAAAAc2V0X2JyZWFrcG9pbnRxDYlYBwAAAHNwZWVkdXBxDkc/8AAAAAAAAFgJ
AAAAc3RhcnRfcG9zcQ9HAAAAAAAAAABYEAAAAHRpbWVzdGFtcF9qaXR0ZXJxEEcAAAAAAAAAAFgG
AAAAdGltaW5ncRFYDQAAAGRldGVybWluaXN0aWNxElgPAAAAdXBkYXRlX2ludGVydmFscRNHP6R6
4UeuFHt1Lg==
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGIWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAACzgAAAOoAAARFAAABtQAAAtYA
AAEJAAAEPQAAAa0AAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxYAQAAADpxDVgOAAAA
c2V0X2JyZWFrcG9pbnRxDolYBAAAAHVuaXRxD1gHAAAAaW5kaWNlc3EQdS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgPAAAAb25saW5lX2Vwb2NoaW5ncQNYDQAAAG1hcmtlci1sb2NrZWRxBFgNAAAAc2FtcGxl
X29mZnNldHEFSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUK
cQdYDAAAAFB5UXQ0LlF0Q29yZXEIWAoAAABRQnl0ZUFycmF5cQlDLgHZ0MsAAQAAAAAB+wAAAMEA
AANyAAABuQAAAgMAAADgAAADagAAAbEAAAAAAABxCoVxC4dxDFJxDVgOAAAAc2VsZWN0X21hcmtl
cnNxDlgNAAAAKHVzZSBkZWZhdWx0KXEPWA4AAABzZXRfYnJlYWtwb2ludHEQiVgLAAAAdGltZV9i
b3VuZHNxEV1xEihK/////0sBZVgHAAAAdmVyYm9zZXETiXUu
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsFSwhLHksgZVgNAAAAbWluaW11bV9waGFzZXEJiFgEAAAAbW9k
ZXEKWAgAAABiYW5kcGFzc3ELWAUAAABvcmRlcnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxDmNzaXAKX3VucGlja2xlX3R5cGUKcQ9YDAAAAFB5UXQ0LlF0Q29y
ZXEQWAoAAABRQnl0ZUFycmF5cRFDLgHZ0MsAAQAAAAACWAAAAXwAAAPPAAACSgAAAmAAAAGbAAAD
xwAAAkIAAAAAAABxEoVxE4dxFFJxFVgOAAAAc2V0X2JyZWFrcG9pbnRxFolYCgAAAHN0b3BfYXR0
ZW5xF0dASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYCgAAAGltYWdfZ3Jh
c3BxB0sAWAwAAABpbWFnX3JlbGVhc2VxCEsBdVgOAAAAbWFwcGluZ19mb3JtYXRxCVgGAAAAY29t
cGF0cQpYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxC2NzaXAKX3VucGlja2xlX3R5cGUKcQxYDAAA
AFB5UXQ0LlF0Q29yZXENWAoAAABRQnl0ZUFycmF5cQ5DLgHZ0MsAAQAAAAAB7wAAAQwAAANmAAAB
vwAAAfcAAAErAAADXgAAAbcAAAAAAABxD4VxEIdxEVJxElgOAAAAc2V0X2JyZWFrcG9pbnRxE4lY
EQAAAHN1cHBvcnRfd2lsZGNhcmRzcRSJWAsAAAB1c2VfbnVtYmVyc3EViVgHAAAAdmVyYm9zZXEW
iXUu
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWBcAAABkZWxheV9zdHJlYW1pbmdfcGFja2V0c3EBiVgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXECY3NpcApfdW5waWNrbGVfdHlwZQpxA1gMAAAAUHlRdDQuUXRDb3JlcQRYCgAAAFFCeXRl
QXJyYXlxBUMuAdnQywABAAAAAAHvAAABJAAAA2YAAAGnAAAB9wAAAUMAAANeAAABnwAAAAAAAHEG
hXEHh3EIUnEJWA4AAABzZXRfYnJlYWtwb2ludHEKiXUu
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWHAAAABDOi9Vc2Vycy9FbW1hbnVlbCBPbGF0ZWp1L0RvY3VtZW50cy9HaXRI
dWIvc2Nob29sIHByb2plY3RzL0VFRTQwMS9MYWIgcmVjb3JkZXIvMTAtMDUtMjAyMS9UZXN0L0Jp
bWJvbGFfUnVuXzEueGRmcQhYEwAAAGhhbmRsZV9jbG9ja19yZXNldHNxCYhYEQAAAGhhbmRsZV9j
bG9ja19zeW5jcQqIWBUAAABoYW5kbGVfaml0dGVyX3JlbW92YWxxC4hYDgAAAG1heF9tYXJrZXJf
bGVucQxYDQAAACh1c2UgZGVmYXVsdClxDVgSAAAAcmVvcmRlcl90aW1lc3RhbXBzcQ6JWA4AAABy
ZXRhaW5fc3RyZWFtc3EPaA1YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlja2xl
X3R5cGUKcRFYDAAAAFB5UXQ0LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDLgHZ0MsAAQAAAAAD
3gAAARAAAAVVAAACJAAAA+YAAAEvAAAFTQAAAhwAAAAAAABxFIVxFYdxFlJxF1gOAAAAc2V0X2Jy
ZWFrcG9pbnRxGIlYDwAAAHVzZV9zdHJlYW1uYW1lc3EZiVgHAAAAdmVyYm9zZXEaiXUu
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWHcAAABDOi9Vc2Vycy9FbW1hbnVlbCBPbGF0ZWp1L0RvY3VtZW50cy9HaXRI
dWIvc2Nob29sIHByb2plY3RzL0VFRTQwMS9MYWIgcmVjb3JkZXIvMTAtMDUtMjAyMS9UcmFpbi9C
aW1ib2xhX1RyaWFsX1J1bl8xLnhkZnEIWBMAAABoYW5kbGVfY2xvY2tfcmVzZXRzcQmIWBEAAABo
YW5kbGVfY2xvY2tfc3luY3EKiFgVAAAAaGFuZGxlX2ppdHRlcl9yZW1vdmFscQuIWA4AAABtYXhf
bWFya2VyX2xlbnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YEgAAAHJlb3JkZXJfdGltZXN0YW1wc3EO
iVgOAAAAcmV0YWluX3N0cmVhbXNxD2gNWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRBjc2lwCl91
bnBpY2tsZV90eXBlCnERWAwAAABQeVF0NC5RdENvcmVxElgKAAAAUUJ5dGVBcnJheXETQy4B2dDL
AAEAAAAAAyAAAAEiAAAElwAAAiAAAAMoAAABQQAABI8AAAIYAAAAAAAAcRSFcRWHcRZScRdYDgAA
AHNldF9icmVha3BvaW50cRiJWA8AAAB1c2Vfc3RyZWFtbmFtZXNxGYlYBwAAAHZlcmJvc2VxGol1
Lg==
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAkAAABpdl9jb2x1bW5xAVgGAAAATWFya2VycQJYDgAAAHBhdHRlcm5fc3ludGF4cQNY
CQAAAHdpbGRjYXJkc3EEWAkAAAByZWdleF9zdWJxBYlYEQAAAHJlbW92ZV9hbGxfb3RoZXJzcQaJ
WAUAAABydWxlc3EHWDIAAAB7J2dyYXNwJzogJ2ltYWdfZ3Jhc3AnLCAncmVsZWFzZSc6ICdpbWFn
X3JlbGVhc2UnfXEIWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBl
CnEKWAwAAABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAAe8AAAEM
AAADZgAAAdoAAAH3AAABKwAAA14AAAHSAAAAAAAAcQ2FcQ6HcQ9ScRBYDgAAAHNldF9icmVha3Bv
aW50cRGJdS4=
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWAkAAABpdl9jb2x1bW5xAVgGAAAATWFya2VycQJYDgAAAHBhdHRlcm5fc3ludGF4cQNY
CQAAAHdpbGRjYXJkc3EEWAkAAAByZWdleF9zdWJxBYlYEQAAAHJlbW92ZV9hbGxfb3RoZXJzcQaJ
WAUAAABydWxlc3EHWDIAAAB7J2dyYXNwJzogJ2ltYWctZ3Jhc3AnLCAncmVsZWFzZSc6ICdpbWFn
X3JlbGVhc2UnfXEIWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBl
CnEKWAwAAABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAAe8AAAEM
AAADZgAAAb8AAAH3AAABKwAAA14AAAG3AAAAAAAAcQ2FcQ6HcQ9ScRBYDgAAAHNldF9icmVha3Bv
aW50cRGJdS4=
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQVjc2lwCl91
bnBpY2tsZV90eXBlCnEGWAwAAABQeVF0NC5RdENvcmVxB1gKAAAAUUJ5dGVBcnJheXEIQy4B2dDL
AAEAAAAAAe8AAAEiAAADZgAAAagAAAH3AAABQQAAA14AAAGgAAAAAAAAcQmFcQqHcQtScQxYDgAA
AHNldF9icmVha3BvaW50cQ2JdS4=
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWAUAAABiYW5kc3EBXXECKF1xAyhLCEsMZV1xBChLDUseZWVYCgAAAGNvbmRfZmllbGRx
BVgLAAAAVGFyZ2V0VmFsdWVxBlgPAAAAaW5pdGlhbGl6ZV9vbmNlcQeIWAwAAABtaW5fZmZ0X3Np
emVxCE0AAVgDAAAAbm9mcQlLBFgOAAAAb3ZlcmxhcF9sZW5ndGhxClgNAAAAKHVzZSBkZWZhdWx0
KXELWAwAAABvdmVybGFwX3VuaXRxDFgHAAAAc2FtcGxlc3ENWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cQ5jc2lwCl91bnBpY2tsZV90eXBlCnEPWAwAAABQeVF0NC5RdENvcmVxEFgKAAAAUUJ5dGVB
cnJheXERQy4B2dDLAAEAAAAAAe8AAAEKAAADZgAAAdsAAAH3AAABKQAAA14AAAHTAAAAAAAAcRKF
cROHcRRScRVYDgAAAHNldF9icmVha3BvaW50cRaJWAkAAABzaHJpbmthZ2VxF0sAWAsAAAB3aW5k
b3dfZnVuY3EYWAQAAABoYW5ucRlYDQAAAHdpbmRvd19sZW5ndGhxGmgLWAwAAAB3aW5kb3dfcGFy
YW1xG2gLWAsAAAB3aW5kb3dfdW5pdHEcWAcAAABzYW1wbGVzcR11Lg==
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAoAAABjb25kX2ZpZWxkcQFYCwAAAFRhcmdldFZhbHVlcQJYDwAAAGluaXRpYWxpemVf
b25jZXEDiFgDAAAAbm9mcQRLBFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNr
bGVfdHlwZQpxBlgMAAAAUHlRdDQuUXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCEMuAdnQywABAAAA
AAHvAAABIgAAA2YAAAGoAAAB9wAAAUEAAANeAAABoAAAAAAAAHEJhXEKh3ELUnEMWA4AAABzZXRf
YnJlYWtwb2ludHENiXUu
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWBcAAABhYnNvbHV0ZV9pbnN0YW5jZV90aW1lc3EBiFgNAAAAY2xvdWRfYWNjb3VudHEC
WAAAAABxA1gMAAAAY2xvdWRfYnVja2V0cQRoA1gRAAAAY2xvdWRfY3JlZGVudGlhbHNxBWgDWAoA
AABjbG91ZF9ob3N0cQZYBwAAAERlZmF1bHRxB1gNAAAAY29sdW1uX2hlYWRlcnEIiFgMAAAAZGVs
ZXRlX3BhcnRzcQmIWAgAAABmaWxlbmFtZXEKWBoAAABCaW1ib2xhX1J1bl8xX3ZhcmlhbmNlLmNz
dnELWAsAAABvdXRwdXRfcm9vdHEMWGEAAABDOi9Vc2Vycy9FbW1hbnVlbCBPbGF0ZWp1L0RvY3Vt
ZW50cy9HaXRIdWIvc2Nob29sIHByb2plY3RzL0VFRTQwMS9GZWF0dXJlc1tFbW1hbnVlbF0vRkJD
U1AvVHJhaW4vcQ1YCwAAAHJldHJpZXZhYmxlcQ6JWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9j
c2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXES
Qy4B2dDLAAEAAAAAAyUAAABuAAAEnAAAAZYAAAMtAAAAjQAABJQAAAGOAAAAAAAAcROFcRSHcRVS
cRZYDgAAAHNldF9icmVha3BvaW50cReJWAsAAAB0aW1lX3N0YW1wc3EYiFgPAAAAdGltZXN0YW1w
X2xhYmVscRlYCQAAAHRpbWVzdGFtcHEadS4=
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWB8AAABCaW1ib2xhX1RyaWFsX1J1bl8xX21hcmtlcnMuY3N2cQhYCwAAAG91
dHB1dF9yb290cQlYYQAAAEM6L1VzZXJzL0VtbWFudWVsIE9sYXRlanUvRG9jdW1lbnRzL0dpdEh1
Yi9zY2hvb2wgcHJvamVjdHMvRUVFNDAxL0ZlYXR1cmVzW0VtbWFudWVsXS9GQkNTUC9UcmFpbi9x
ClgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXELY3NpcApfdW5waWNrbGVfdHlwZQpxDFgMAAAAUHlR
dDQuUXRDb3JlcQ1YCgAAAFFCeXRlQXJyYXlxDkMuAdnQywABAAAAAAJ8AAAAuwAAA/MAAAHRAAAC
hAAAANoAAAPrAAAByQAAAAAAAHEPhXEQh3ERUnESWA4AAABzZXRfYnJlYWtwb2ludHETiVgGAAAA
c3RyZWFtcRRYDQAAACh1c2UgZGVmYXVsdClxFXUu
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWAwAAABpbml0aWFsX2RpbXNxAl1xAyhLMksyTfQB
TfQBZVgOAAAAb3ZlcnJpZGVfc3JhdGVxBFgNAAAAKHVzZSBkZWZhdWx0KXEFWBMAAABzYXZlZFdp
ZGdldEdlb21ldHJ5cQZjc2lwCl91bnBpY2tsZV90eXBlCnEHWAwAAABQeVF0NC5RdENvcmVxCFgK
AAAAUUJ5dGVBcnJheXEJQy4B2dDLAAEAAAAAAe8AAAEYAAADZgAAAbMAAAH3AAABNwAAA14AAAGr
AAAAAAAAcQqFcQuHcQxScQ1YDgAAAHNldF9icmVha3BvaW50cQ6JWAsAAABzdHJlYW1fbmFtZXEP
WAcAAABNYXJrZXJzcRB1Lg==
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWBkAAABCaW1ib2xhX1J1bl8xX21hcmtlcnMuY3N2cQhYCwAAAG91dHB1dF9y
b290cQlYYAAAAEM6L1VzZXJzL0VtbWFudWVsIE9sYXRlanUvRG9jdW1lbnRzL0dpdEh1Yi9zY2hv
b2wgcHJvamVjdHMvRUVFNDAxL0ZlYXR1cmVzW0VtbWFudWVsXS9GQkNTUC9UZXN0L3EKWBMAAABz
YXZlZFdpZGdldEdlb21ldHJ5cQtjc2lwCl91bnBpY2tsZV90eXBlCnEMWAwAAABQeVF0NC5RdENv
cmVxDVgKAAAAUUJ5dGVBcnJheXEOQy4B2dDLAAEAAAAAA94AAACjAAAFVQAAAbkAAAPmAAAAwgAA
BU0AAAGxAAAAAAAAcQ+FcRCHcRFScRJYDgAAAHNldF9icmVha3BvaW50cROJWAYAAABzdHJlYW1x
FFgNAAAAKHVzZSBkZWZhdWx0KXEVdS4=
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYDAAAAFRlc3QtbWFya2Vyc3EEWBAAAABtYXJrZXJfc291cmNlX2lkcQVY
AAAAAHEGWAwAAABtYXhfYnVmZmVyZWRxB0s8WBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEI
iVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEJY3NpcApfdW5waWNrbGVfdHlwZQpxClgMAAAAUHlR
dDQuUXRDb3JlcQtYCgAAAFFCeXRlQXJyYXlxDEMuAdnQywABAAAAAAHvAAAApgAAA2YAAAIlAAAB
9wAAAMUAAANeAAACHQAAAAAAAHENhXEOh3EPUnEQWAwAAABzZW5kX21hcmtlcnNxEYhYDgAAAHNl
dF9icmVha3BvaW50cRKJWAkAAABzb3VyY2VfaWRxE1gEAAAAVGVzdHEUWAUAAABzcmF0ZXEVWA0A
AAAodXNlIGRlZmF1bHQpcRZYCwAAAHN0cmVhbV9uYW1lcRdYCgAAAFRlc3RTdHJlYW1xGFgLAAAA
c3RyZWFtX3R5cGVxGVgDAAAARUVHcRpYEwAAAHVzZV9kYXRhX3RpbWVzdGFtcHNxG4hYFgAAAHVz
ZV9udW1weV9vcHRpbWl6YXRpb25xHIl1Lg==
</properties>
		<properties format="pickle" node_id="18">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgTAAAAbmFtZT0nVGVzdC1tYXJrZXJzJ3EFWAwAAABtYXhfYmxvY2tsZW5xBk0A
BFgKAAAAbWF4X2J1ZmxlbnEHSx5YDAAAAG1heF9jaHVua2xlbnEISwBYDAAAAG5vbWluYWxfcmF0
ZXEJWA0AAAAodXNlIGRlZmF1bHQpcQpYBQAAAHF1ZXJ5cQtYEQAAAG5hbWU9J1Rlc3RTdHJlYW0n
cQxYBwAAAHJlY292ZXJxDYhYFAAAAHJlc29sdmVfbWluaW11bV90aW1lcQ5HP+AAAAAAAABYEwAA
AHNhdmVkV2lkZ2V0R2VvbWV0cnlxD2NzaXAKX3VucGlja2xlX3R5cGUKcRBYDAAAAFB5UXQ0LlF0
Q29yZXERWAoAAABRQnl0ZUFycmF5cRJDLgHZ0MsAAQAAAAAB7wAAAQAAAANmAAABywAAAfcAAAEf
AAADXgAAAcMAAAAAAABxE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4l1Lg==
</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlj
a2xlX3R5cGUKcQVYDAAAAFB5UXQ0LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAA
AAAB7wAAAS4AAANmAAABnAAAAfcAAAFNAAADXgAAAZQAAAAAAABxCIVxCYdxClJxC1gOAAAAc2V0
X2JyZWFrcG9pbnRxDIlYDgAAAHdhcm11cF9zYW1wbGVzcQ1K/////3Uu
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKJWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4hYDAAAAGN1c3RvbV9sYWJlbHEEWA0AAAAodXNlIGRlZmF1
bHQpcQVYCQAAAGluaXRfZGF0YXEGXXEHKFgDAAAAQTFBcQhYAwAAAEEyQXEJWAMAAABBM0FxClgD
AAAAQTRBcQtYAwAAAEE0QnEMWAMAAABBM0JxDVgDAAAAQTJCcQ5YAwAAAEExQnEPWAMAAABCMUFx
EFgDAAAAQjJBcRFYAwAAAEIzQXESWAMAAABCNEFxE1gDAAAAQjRCcRRYAwAAAEIzQnEVWAMAAABC
MkJxFlgDAAAAQjFCcRdlWAgAAABuZXdfYXhpc3EYWAUAAABzcGFjZXEZWAgAAABvbGRfYXhpc3Ea
WAcAAABmZWF0dXJlcRtYDAAAAG9ubHlfc2lnbmFsc3EciFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEdY3NpcApfdW5waWNrbGVfdHlwZQpxHlgMAAAAUHlRdDQuUXRDb3JlcR9YCgAAAFFCeXRlQXJy
YXlxIEMuAdnQywABAAAAAAcsAAAA7wAACKMAAAJ/AAAHNAAAAQ4AAAibAAACdwAAAAEAAHEhhXEi
h3EjUnEkWA4AAABzZXRfYnJlYWtwb2ludHEliXUu
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
            "node4",
            "data",
            "node3",
            "data"
        ],
        [
            "node5",
            "data",
            "node2",
            "data"
        ],
        [
            "node6",
            "data",
            "node5",
            "data"
        ],
        [
            "node9",
            "data",
            "node6",
            "calib_data"
        ],
        [
            "node8",
            "data",
            "node9",
            "data"
        ],
        [
            "node8",
            "data",
            "node15",
            "data"
        ],
        [
            "node10",
            "data",
            "node1",
            "data"
        ],
        [
            "node10",
            "data",
            "node17",
            "data"
        ],
        [
            "node2",
            "data",
            "node4",
            "data"
        ],
        [
            "node3",
            "data",
            "node16",
            "data"
        ],
        [
            "node3",
            "data",
            "node12",
            "data"
        ],
        [
            "node1",
            "data",
            "node18",
            "data"
        ],
        [
            "node7",
            "data",
            "node20",
            "data"
        ],
        [
            "node20",
            "data",
            "node10",
            "data"
        ],
        [
            "node12",
            "data",
            "node11",
            "data"
        ],
        [
            "node11",
            "data",
            "node21",
            "data"
        ],
        [
            "node21",
            "data",
            "node14",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
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
            "uuid": "236e3f70-e4be-48b1-a0bc-5c5487e351cf"
        },
        "node10": {
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
            "uuid": "a4197cb1-6a67-48de-831f-1c4809bde65c"
        },
        "node11": {
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
            "uuid": "adaa55f2-0498-4ccb-bed6-748acc01c404"
        },
        "node12": {
            "class": "FilterBankCommonSpatialPattern",
            "module": "neuropype.nodes.neural.FilterBankCommonSpatialPattern",
            "params": {
                "bands": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        [
                            8,
                            12
                        ],
                        [
                            13,
                            30
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
                    "customized": true,
                    "type": "IntPort",
                    "value": 4
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
            "uuid": "7b7c80ea-4c68-47ef-b526-dd8aad4542b1"
        },
        "node13": {
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
            "uuid": "9062a10e-268e-422e-ba5d-8eb8d18ea3df"
        },
        "node14": {
            "class": "RecordToCSV",
            "module": "neuropype.nodes.file_system.RecordToCSV",
            "params": {
                "absolute_instance_times": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
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
                "column_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Bimbola_Run_1_variance.csv"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Features[Emmanuel]/FBCSP/Train/"
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_stamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "timestamp_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "timestamp"
                }
            },
            "uuid": "375d7981-9967-4b19-ba42-42b593f8e3ce"
        },
        "node15": {
            "class": "ExportMarkers",
            "module": "neuropype.nodes.markers.ExportMarkers",
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
                    "value": "Bimbola_Trial_Run_1_markers.csv"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Features[Emmanuel]/FBCSP/Train/"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                }
            },
            "uuid": "a23e5a45-3ea1-40d1-a69d-b206533135b5"
        },
        "node16": {
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
            "uuid": "102e9449-caad-4631-b88e-956f26e4c068"
        },
        "node17": {
            "class": "ExportMarkers",
            "module": "neuropype.nodes.markers.ExportMarkers",
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
                    "value": "Bimbola_Run_1_markers.csv"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Features[Emmanuel]/FBCSP/Test/"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                }
            },
            "uuid": "164cf91b-331a-47cd-b87e-9622b8def7da"
        },
        "node18": {
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
                    "value": "Test-markers"
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
                    "value": "Test"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "TestStream"
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
            "uuid": "7478375d-0518-4cf6-8c20-585dffd8d11f"
        },
        "node19": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='Test-markers'"
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='TestStream'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "b09d5f61-5773-49ac-b125-4868e6dd60ae"
        },
        "node2": {
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
            "uuid": "8b291910-9ac0-42d1-a217-60f640e8ca43"
        },
        "node20": {
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
            "uuid": "71323f30-d8fe-4ea4-9240-24334e7a7c1a"
        },
        "node21": {
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
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "A1A",
                        "A2A",
                        "A3A",
                        "A4A",
                        "A4B",
                        "A3B",
                        "A2B",
                        "A1B",
                        "B1A",
                        "B2A",
                        "B3A",
                        "B4A",
                        "B4B",
                        "B3B",
                        "B2B",
                        "B1B"
                    ]
                },
                "new_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
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
            "uuid": "0036700c-828c-40f4-b062-d4eebd5ee55b"
        },
        "node3": {
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
            "uuid": "7505aa50-077b-47bd-85f6-e993f1332e94"
        },
        "node4": {
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
            "uuid": "e41c19aa-03bf-4c31-83ea-997af96e28c7"
        },
        "node5": {
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
            "uuid": "7bc99b22-f47a-4557-afbe-d8a92b0d7def"
        },
        "node6": {
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
            "uuid": "d6de3ed8-62d6-4d5c-a598-15caed206612"
        },
        "node7": {
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
                    "value": "C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Lab recorder/10-05-2021/Test/Bimbola_Run_1.xdf"
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
            "uuid": "12ec016e-cf7c-4772-a39d-67db44ebf90b"
        },
        "node8": {
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
                    "value": "C:/Users/Emmanuel Olateju/Documents/GitHub/school projects/EEE401/Lab recorder/10-05-2021/Train/Bimbola_Trial_Run_1.xdf"
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
            "uuid": "2a448767-54c7-4013-80af-951b2ee20a31"
        },
        "node9": {
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
            "uuid": "9c4d3bc3-8ce2-4f4a-a43f-800d02fe24f5"
        }
    },
    "version": 1.1
}</patch>
</scheme>
