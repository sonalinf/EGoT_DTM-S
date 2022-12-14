#include "include/trust_cta2045/trust_ucm.hpp"
#include <iostream>
#include <https/single_client.hpp>
#include <trust_xml/trust_xml.hpp>
#include <utilities/utilities.hpp>

using namespace cea2045;

namespace trust
{
    cea2045UCM::cea2045UCM()
    {
        max_payload_ = cea2045::MaxPayloadLengthCode::LENGTH2;
    }

    cea2045UCM::~cea2045UCM()
    {
        // do nothing
    }

    bool cea2045UCM::isMessageTypeSupported(MessageTypeCode type_code)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "isMessageTypeSupported";
        msg.contents["MessageTypeCode"] = psu::utilities::ToUnderlyingType(type_code);
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));

        if (type_code == MessageTypeCode::NONE)
        {
            return false;
        }

        return true;
    }

    MaxPayloadLengthCode cea2045UCM::getMaxPayload()
    {
        return max_payload_;
    }

    void cea2045UCM::processMaxPayloadResponse(MaxPayloadLengthCode payload)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processMaxPayloadResponse";
        msg.contents["MaxPayloadLengthCode"] = psu::utilities::ToUnderlyingType(max_payload_);
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));

        max_payload_ = payload;
    }

    void cea2045UCM::processDeviceInfoResponse(cea2045DeviceInfoResponse *message)
    {
        // device_info_ = *message;
        device_info_.device_type = message->getDeviceType();
        device_info_.capability_map = (uint64_t)message->capability;
        device_info_.vendor_id = message->getVendorID();
        device_info_.firmware_day = (uint32_t)message->firmwareDay;
        device_info_.firmware_month = (uint32_t)message->firmwareMonth;
        device_info_.firmware_year = 2000 + (uint32_t)message->firmwareYear20xx;
        device_info_.firmware_minor = (uint32_t)message->firmwareMinor;
        device_info_.firmware_major = (uint32_t)message->firmwareMajor;

        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processDeviceInfoResponse";
        msg.contents["deviceType"] = device_info_.device_type;
        msg.contents["capability"] = device_info_.capability_map;
        msg.contents["vendorId"] = device_info_.vendor_id;
        msg.contents["firmwareDay"] = device_info_.firmware_day;
        msg.contents["firmwareMonth"] = device_info_.firmware_month;
        msg.contents["firmwareYear"] = device_info_.firmware_year;
        msg.contents["firmwareMinor"] = device_info_.firmware_minor;
        msg.contents["firmwareMajor"] = device_info_.firmware_major;
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processCommodityResponse(cea2045CommodityResponse *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processCommodityResponse";

        size_t count = message->getCommodityDataCount();
        for (size_t i = 0; i < count; i++)
        {
            cea2045CommodityData data = *message->getCommodityData(i);
            commodities_[(uint8_t)data.commodityCode] = data;
            
            msg.contents["commodityCode:"+data.commodityCode] = data.commodityCode;
            msg.contents[data.commodityCode+":instantaneousRate"] = data.getInstantaneousRate();
            msg.contents[data.commodityCode+":cumulativeAmount"] = data.getCumulativeAmount();
        }

        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processSetEnergyPriceResponse(cea2045IntermediateResponse *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processSetEnergyPriceResponse";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processSetTemperatureOffsetResponse(cea2045IntermediateResponse *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processSetTemperatureOffsetResponse";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processGetTemperatureOffsetResponse(cea2045GetTemperateOffsetResponse *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processGetTemperatureOffsetResponse";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processSetSetpointsResponse(cea2045IntermediateResponse *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processSetSetpointsResponse";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processGetSetpointsResponse(cea2045GetSetpointsResponse1 *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processGetSetpointsResponse";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processGetSetpointsResponse(cea2045GetSetpointsResponse2 *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processGetSetpointsResponse";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processStartCyclingResponse(cea2045IntermediateResponse *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processStartCyclingResponse";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processTerminateCyclingResponse(cea2045IntermediateResponse *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processTerminateCyclingResponse";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processGetPresentTemperatureResponse(cea2045GetPresentTemperatureResponse *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processGetPresentTemperatureResponse";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processGetUTCTimeResponse(cea2045GetUTCTimeResponse *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processGetUTCTimeResponse";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processAckReceived(MessageCode code)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processAckReceived";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processNakReceived(LinkLayerNakCode nak, MessageCode code)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processNakReceived";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processAppAckReceived(cea2045Basic *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processAppAckReceived";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processAppNakReceived(cea2045Basic *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processAppNakReceived";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processOperationalStateReceived(cea2045Basic *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processOperationalStateReceived";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processAppCustomerOverride(cea2045Basic *message)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processAppCustomerOverride";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

    void cea2045UCM::processIncompleteMessage(const unsigned char *buffer, unsigned int byte_count)
    {
        trust::Message msg;
        msg.to = "DCM";
        msg.from = "DER";
        msg.timestamp = psu::utilities::getTime();
        msg.contents["response"] = "processIncompleteMessage";
        https::SingleClient::getInstance().Post("", trust::Stringify(msg));
    }

} // namespace trust
