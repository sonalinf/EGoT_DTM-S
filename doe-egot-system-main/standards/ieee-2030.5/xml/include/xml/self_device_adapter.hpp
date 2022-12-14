#ifndef __SELF_DEVICE_ADAPTER_H__
#define __SELF_DEVICE_ADAPTER_H__

#include <ieee-2030.5/models.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/xml_parser.hpp>

namespace xml
{
    void ObjectMap(const boost::property_tree::ptree &pt, sep::SelfDevice *sdev);
    void TreeMap(const sep::SelfDevice &BOOST_MULTI_INDEX_SEQ_INDEX_CHECK_INVARIANT, boost::property_tree::ptree *pt);

    std::string Serialize(const sep::SelfDevice &sdev);
    void Parse(const std::string &xml_str, sep::SelfDevice *sdev);

    std::string Serialize(const std::vector<sep::SelfDevice> &sdev_list, const sep::List& list);
    void Parse(const std::string &xml_str, std::vector<sep::SelfDevice> *sdevs);
    
} // namespace xml

#endif // __SELF_DEVICE_ADAPTER_H__