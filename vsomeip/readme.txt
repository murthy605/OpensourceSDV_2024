

To start the request/response-example from the build-directory do:


HOST1: env VSOMEIP_CONFIGURATION=../../config/vsomeip-local.json VSOMEIP_APPLICATION_NAME=client-sample ./subscribe-sample
HOST1: env VSOMEIP_CONFIGURATION=../../config/vsomeip-local.json VSOMEIP_APPLICATION_NAME=service-sample ./notify-sample
