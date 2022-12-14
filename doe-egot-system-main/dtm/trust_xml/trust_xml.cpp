#include "include/trust_xml/trust_xml.hpp"
#include <boost/property_tree/xml_parser.hpp>

namespace pt = boost::property_tree;

namespace trust
{
    boost::property_tree::ptree Treeify(const std::string &xml_str)
    {
        // utility function to help translate strings to/from objects
        std::stringstream ss (xml_str);
        boost::property_tree::ptree pt;
        boost::property_tree::xml_parser::read_xml(ss, pt);
        return pt;
    };
    
    boost::property_tree::ptree Treeify(const Message& message)
    {
        pt::ptree tree;
        tree.put("message.to", message.to);
        tree.put("message.from", message.from);
        
        for (const auto& arg : message.contents)
        {
            if (arg.first == "body"){
                pt::ptree body = Treeify(arg.second);
                tree.put_child("message.contents."+arg.first, body);
            }
            else {
                tree.put("message.contents."+arg.first, arg.second);
            }   
        }  

        return tree;
    };

    std::string Stringify(const boost::property_tree::ptree &pt)
    {
        // utility function to help translate strings to/from objects
        std::stringstream ss;
        boost::property_tree::xml_parser::write_xml(ss, pt);
        return ss.str();
    };

    std::string Stringify(const Message& message)
    {
        // utility function to help translate strings to/from objects
        return Stringify(Treeify(message));
    };
}