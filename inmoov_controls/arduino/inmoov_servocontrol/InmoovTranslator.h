#ifndef _ROS_SERVICE_InmoovTranslator_h
#define _ROS_SERVICE_InmoovTranslator_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace inmoov_controls
{

static const char INMOOVTRANSLATOR[] = "inmoov_controls/InmoovTranslator";

  class InmoovTranslatorRequest : public ros::Msg
  {
    public:
      typedef const char* _joint_type;
      _joint_type joint;

    InmoovTranslatorRequest():
      joint("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t length_joint = strlen(this->joint);
      varToArr(outbuffer + offset, length_joint);
      offset += 4;
      memcpy(outbuffer + offset, this->joint, length_joint);
      offset += length_joint;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_joint;
      arrToVar(length_joint, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_joint; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_joint-1]=0;
      this->joint = (char *)(inbuffer + offset-1);
      offset += length_joint;
     return offset;
    }

    const char * getType(){ return INMOOVTRANSLATOR; };
    const char * getMD5(){ return "23b081b5cb543c8335b9afac2f3e238c"; };

  };

  class InmoovTranslatorResponse : public ros::Msg
  {
    public:
      typedef int64_t _pin_type;
      _pin_type pin;

    InmoovTranslatorResponse():
      pin(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int64_t real;
        uint64_t base;
      } u_pin;
      u_pin.real = this->pin;
      *(outbuffer + offset + 0) = (u_pin.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_pin.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_pin.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_pin.base >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (u_pin.base >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (u_pin.base >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (u_pin.base >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (u_pin.base >> (8 * 7)) & 0xFF;
      offset += sizeof(this->pin);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int64_t real;
        uint64_t base;
      } u_pin;
      u_pin.base = 0;
      u_pin.base |= ((uint64_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_pin.base |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_pin.base |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_pin.base |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      u_pin.base |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      u_pin.base |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      u_pin.base |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      u_pin.base |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      this->pin = u_pin.real;
      offset += sizeof(this->pin);
     return offset;
    }

    const char * getType(){ return INMOOVTRANSLATOR; };
    const char * getMD5(){ return "13ce2e1fd6796d00dec37deecb854c69"; };

  };

  class InmoovTranslator {
    public:
    typedef InmoovTranslatorRequest Request;
    typedef InmoovTranslatorResponse Response;
  };

}
#endif
