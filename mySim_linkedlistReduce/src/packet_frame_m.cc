//
// Generated file, do not edit! Created by nedtool 5.6 from src/packet_frame.msg.
//

// Disable warnings about unused variables, empty switch stmts, etc:
#ifdef _MSC_VER
#pragma warning(disable : 4101)
#pragma warning(disable : 4065)
#endif

#if defined(__clang__)
#pragma clang diagnostic ignored "-Wshadow"
#pragma clang diagnostic ignored "-Wconversion"
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wc++98-compat"
#pragma clang diagnostic ignored "-Wunreachable-code-break"
#pragma clang diagnostic ignored "-Wold-style-cast"
#elif defined(__GNUC__)
#pragma GCC diagnostic ignored "-Wshadow"
#pragma GCC diagnostic ignored "-Wconversion"
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wold-style-cast"
#pragma GCC diagnostic ignored "-Wsuggest-attribute=noreturn"
#pragma GCC diagnostic ignored "-Wfloat-conversion"
#endif

#include <iostream>
#include <sstream>
#include "packet_frame_m.h"

namespace omnetpp
{

    // Template pack/unpack rules. They are declared *after* a1l type-specific pack functions for multiple reasons.
    // They are in the omnetpp namespace, to allow them to be found by argument-dependent lookup via the cCommBuffer argument

    // Packing/unpacking an std::vector
    template <typename T, typename A>
    void doParsimPacking(omnetpp::cCommBuffer *buffer, const std::vector<T, A> &v)
    {
        int n = v.size();
        doParsimPacking(buffer, n);
        for (int i = 0; i < n; i++)
            doParsimPacking(buffer, v[i]);
    }

    template <typename T, typename A>
    void doParsimUnpacking(omnetpp::cCommBuffer *buffer, std::vector<T, A> &v)
    {
        int n;
        doParsimUnpacking(buffer, n);
        v.resize(n);
        for (int i = 0; i < n; i++)
            doParsimUnpacking(buffer, v[i]);
    }

    // Packing/unpacking an std::list
    template <typename T, typename A>
    void doParsimPacking(omnetpp::cCommBuffer *buffer, const std::list<T, A> &l)
    {
        doParsimPacking(buffer, (int)l.size());
        for (typename std::list<T, A>::const_iterator it = l.begin(); it != l.end(); ++it)
            doParsimPacking(buffer, (T &)*it);
    }

    template <typename T, typename A>
    void doParsimUnpacking(omnetpp::cCommBuffer *buffer, std::list<T, A> &l)
    {
        int n;
        doParsimUnpacking(buffer, n);
        for (int i = 0; i < n; i++)
        {
            l.push_back(T());
            doParsimUnpacking(buffer, l.back());
        }
    }

    // Packing/unpacking an std::set
    template <typename T, typename Tr, typename A>
    void doParsimPacking(omnetpp::cCommBuffer *buffer, const std::set<T, Tr, A> &s)
    {
        doParsimPacking(buffer, (int)s.size());
        for (typename std::set<T, Tr, A>::const_iterator it = s.begin(); it != s.end(); ++it)
            doParsimPacking(buffer, *it);
    }

    template <typename T, typename Tr, typename A>
    void doParsimUnpacking(omnetpp::cCommBuffer *buffer, std::set<T, Tr, A> &s)
    {
        int n;
        doParsimUnpacking(buffer, n);
        for (int i = 0; i < n; i++)
        {
            T x;
            doParsimUnpacking(buffer, x);
            s.insert(x);
        }
    }

    // Packing/unpacking an std::map
    template <typename K, typename V, typename Tr, typename A>
    void doParsimPacking(omnetpp::cCommBuffer *buffer, const std::map<K, V, Tr, A> &m)
    {
        doParsimPacking(buffer, (int)m.size());
        for (typename std::map<K, V, Tr, A>::const_iterator it = m.begin(); it != m.end(); ++it)
        {
            doParsimPacking(buffer, it->first);
            doParsimPacking(buffer, it->second);
        }
    }

    template <typename K, typename V, typename Tr, typename A>
    void doParsimUnpacking(omnetpp::cCommBuffer *buffer, std::map<K, V, Tr, A> &m)
    {
        int n;
        doParsimUnpacking(buffer, n);
        for (int i = 0; i < n; i++)
        {
            K k;
            V v;
            doParsimUnpacking(buffer, k);
            doParsimUnpacking(buffer, v);
            m[k] = v;
        }
    }

    // Default pack/unpack function for arrays
    template <typename T>
    void doParsimArrayPacking(omnetpp::cCommBuffer *b, const T *t, int n)
    {
        for (int i = 0; i < n; i++)
            doParsimPacking(b, t[i]);
    }

    template <typename T>
    void doParsimArrayUnpacking(omnetpp::cCommBuffer *b, T *t, int n)
    {
        for (int i = 0; i < n; i++)
            doParsimUnpacking(b, t[i]);
    }

    // Default rule to prevent compiler from choosing base class' doParsimPacking() function
    template <typename T>
    void doParsimPacking(omnetpp::cCommBuffer *, const T &t)
    {
        throw omnetpp::cRuntimeError("Parsim error: No doParsimPacking() function for type %s", omnetpp::opp_typename(typeid(t)));
    }

    template <typename T>
    void doParsimUnpacking(omnetpp::cCommBuffer *, T &t)
    {
        throw omnetpp::cRuntimeError("Parsim error: No doParsimUnpacking() function for type %s", omnetpp::opp_typename(typeid(t)));
    }

} // namespace omnetpp

// forward
template <typename T, typename A>
std::ostream &operator<<(std::ostream &out, const std::vector<T, A> &vec);

// Template rule which fires if a struct or class doesn't have operator<<
template <typename T>
inline std::ostream &operator<<(std::ostream &out, const T &) { return out; }

// operator<< for std::vector<T>
template <typename T, typename A>
inline std::ostream &operator<<(std::ostream &out, const std::vector<T, A> &vec)
{
    out.put('{');
    for (typename std::vector<T, A>::const_iterator it = vec.begin(); it != vec.end(); ++it)
    {
        if (it != vec.begin())
        {
            out.put(',');
            out.put(' ');
        }
        out << *it;
    }
    out.put('}');

    char buf[32];
    sprintf(buf, " (size=%u)", (unsigned int)vec.size());
    out.write(buf, strlen(buf));
    return out;
}

Register_Class(packet_frame)

    packet_frame::packet_frame(const char *name, short kind) : ::omnetpp::cPacket(name, kind)
{
    this->dest_id = 0;
    this->source_id = 0;
    this->sender_id = 0;
    this->msg_type = 0;
    this->msg_id = 0;
    this->charge_cycle = 0;
    this->origin_slot = 0;
    this->current_slot = 0;
    this->lag_bias = 0;
    this->delay_bias = 0;
    this->sender_type = 0;
    this->next_id = 0;
    this->pass_counter = 0;
    this->node_state = 0;
    this->send_time = 0;
}

packet_frame::packet_frame(const packet_frame &other) : ::omnetpp::cPacket(other)
{
    copy(other);
}

packet_frame::~packet_frame()
{
}

packet_frame &packet_frame::operator=(const packet_frame &other)
{
    if (this == &other)
        return *this;
    ::omnetpp::cPacket::operator=(other);
    copy(other);
    return *this;
}

void packet_frame::copy(const packet_frame &other)
{
    this->dest_id = other.dest_id;
    this->source_id = other.source_id;
    this->sender_id = other.sender_id;
    this->msg_type = other.msg_type;
    this->msg_id = other.msg_id;
    this->charge_cycle = other.charge_cycle;
    this->origin_slot = other.origin_slot;
    this->current_slot = other.current_slot;
    this->lag_bias = other.lag_bias;
    this->delay_bias = other.delay_bias;
    this->sender_type = other.sender_type;
    this->next_id = other.next_id;
    this->pass_counter = other.pass_counter;
    this->node_state = other.node_state;
    this->send_time = other.send_time;
}

void packet_frame::parsimPack(omnetpp::cCommBuffer *b) const
{
    ::omnetpp::cPacket::parsimPack(b);
    doParsimPacking(b, this->dest_id);
    doParsimPacking(b, this->source_id);
    doParsimPacking(b, this->sender_id);
    doParsimPacking(b, this->msg_type);
    doParsimPacking(b, this->msg_id);
    doParsimPacking(b, this->charge_cycle);
    doParsimPacking(b, this->origin_slot);
    doParsimPacking(b, this->current_slot);
    doParsimPacking(b, this->lag_bias);
    doParsimPacking(b, this->delay_bias);
    doParsimPacking(b, this->sender_type);
    doParsimPacking(b, this->next_id);
    doParsimPacking(b, this->pass_counter);
    doParsimPacking(b, this->node_state);
    doParsimPacking(b, this->send_time);
}

void packet_frame::parsimUnpack(omnetpp::cCommBuffer *b)
{
    ::omnetpp::cPacket::parsimUnpack(b);
    doParsimUnpacking(b, this->dest_id);
    doParsimUnpacking(b, this->source_id);
    doParsimUnpacking(b, this->sender_id);
    doParsimUnpacking(b, this->msg_type);
    doParsimUnpacking(b, this->msg_id);
    doParsimUnpacking(b, this->charge_cycle);
    doParsimUnpacking(b, this->origin_slot);
    doParsimUnpacking(b, this->current_slot);
    doParsimUnpacking(b, this->lag_bias);
    doParsimUnpacking(b, this->delay_bias);
    doParsimUnpacking(b, this->sender_type);
    doParsimUnpacking(b, this->next_id);
    doParsimUnpacking(b, this->pass_counter);
    doParsimUnpacking(b, this->node_state);
    doParsimUnpacking(b, this->send_time);
}

int packet_frame::getDest_id() const
{
    return this->dest_id;
}

void packet_frame::setDest_id(int dest_id)
{
    this->dest_id = dest_id;
}

int packet_frame::getSource_id() const
{
    return this->source_id;
}

void packet_frame::setSource_id(int source_id)
{
    this->source_id = source_id;
}

int packet_frame::getSender_id() const
{
    return this->sender_id;
}

void packet_frame::setSender_id(int sender_id)
{
    this->sender_id = sender_id;
}

int packet_frame::getMsg_type() const
{
    return this->msg_type;
}

void packet_frame::setMsg_type(int msg_type)
{
    this->msg_type = msg_type;
}

int packet_frame::getMsg_id() const
{
    return this->msg_id;
}

void packet_frame::setMsg_id(int msg_id)
{
    this->msg_id = msg_id;
}

int packet_frame::getCharge_cycle() const
{
    return this->charge_cycle;
}

void packet_frame::setCharge_cycle(int charge_cycle)
{
    this->charge_cycle = charge_cycle;
}

int packet_frame::getOrigin_slot() const
{
    return this->origin_slot;
}

void packet_frame::setOrigin_slot(int origin_slot)
{
    this->origin_slot = origin_slot;
}

int packet_frame::getCurrent_slot() const
{
    return this->current_slot;
}

void packet_frame::setCurrent_slot(int current_slot)
{
    this->current_slot = current_slot;
}

int packet_frame::getLag_bias() const
{
    return this->lag_bias;
}

void packet_frame::setLag_bias(int lag_bias)
{
    this->lag_bias = lag_bias;
}

int packet_frame::getDelay_bias() const
{
    return this->delay_bias;
}

void packet_frame::setDelay_bias(int delay_bias)
{
    this->delay_bias = delay_bias;
}

int packet_frame::getSender_type() const
{
    return this->sender_type;
}

void packet_frame::setSender_type(int sender_type)
{
    this->sender_type = sender_type;
}

int packet_frame::getNext_id() const
{
    return this->next_id;
}

void packet_frame::setNext_id(int next_id)
{
    this->next_id = next_id;
}

int packet_frame::getPass_counter() const
{
    return this->pass_counter;
}

void packet_frame::setPass_counter(int pass_counter)
{
    this->pass_counter = pass_counter;
}

int packet_frame::getNode_state() const
{
    return this->node_state;
}

void packet_frame::setNode_state(int node_state)
{
    this->node_state = node_state;
}

::omnetpp::simtime_t packet_frame::getSend_time() const
{
    return this->send_time;
}

void packet_frame::setSend_time(::omnetpp::simtime_t send_time)
{
    this->send_time = send_time;
}

class packet_frameDescriptor : public omnetpp::cClassDescriptor
{
private:
    mutable const char **propertynames;

public:
    packet_frameDescriptor();
    virtual ~packet_frameDescriptor();

    virtual bool doesSupport(omnetpp::cObject *obj) const override;
    virtual const char **getPropertyNames() const override;
    virtual const char *getProperty(const char *propertyname) const override;
    virtual int getFieldCount() const override;
    virtual const char *getFieldName(int field) const override;
    virtual int findField(const char *fieldName) const override;
    virtual unsigned int getFieldTypeFlags(int field) const override;
    virtual const char *getFieldTypeString(int field) const override;
    virtual const char **getFieldPropertyNames(int field) const override;
    virtual const char *getFieldProperty(int field, const char *propertyname) const override;
    virtual int getFieldArraySize(void *object, int field) const override;

    virtual const char *getFieldDynamicTypeString(void *object, int field, int i) const override;
    virtual std::string getFieldValueAsString(void *object, int field, int i) const override;
    virtual bool setFieldValueAsString(void *object, int field, int i, const char *value) const override;

    virtual const char *getFieldStructName(int field) const override;
    virtual void *getFieldStructValuePointer(void *object, int field, int i) const override;
};

Register_ClassDescriptor(packet_frameDescriptor)

    packet_frameDescriptor::packet_frameDescriptor() : omnetpp::cClassDescriptor("packet_frame", "omnetpp::cPacket")
{
    propertynames = nullptr;
}

packet_frameDescriptor::~packet_frameDescriptor()
{
    delete[] propertynames;
}

bool packet_frameDescriptor::doesSupport(omnetpp::cObject *obj) const
{
    return dynamic_cast<packet_frame *>(obj) != nullptr;
}

const char **packet_frameDescriptor::getPropertyNames() const
{
    if (!propertynames)
    {
        static const char *names[] = {nullptr};
        omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
        const char **basenames = basedesc ? basedesc->getPropertyNames() : nullptr;
        propertynames = mergeLists(basenames, names);
    }
    return propertynames;
}

const char *packet_frameDescriptor::getProperty(const char *propertyname) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    return basedesc ? basedesc->getProperty(propertyname) : nullptr;
}

int packet_frameDescriptor::getFieldCount() const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    return basedesc ? 15 + basedesc->getFieldCount() : 15;
}

unsigned int packet_frameDescriptor::getFieldTypeFlags(int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldTypeFlags(field);
        field -= basedesc->getFieldCount();
    }
    static unsigned int fieldTypeFlags[] = {
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
        FD_ISEDITABLE,
    };
    return (field >= 0 && field < 15) ? fieldTypeFlags[field] : 0;
}

const char *packet_frameDescriptor::getFieldName(int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldName(field);
        field -= basedesc->getFieldCount();
    }
    static const char *fieldNames[] = {
        "dest_id",
        "source_id",
        "sender_id",
        "msg_type",
        "msg_id",
        "charge_cycle",
        "origin_slot",
        "current_slot",
        "lag_bias",
        "delay_bias",
        "sender_type",
        "next_id",
        "pass_counter",
        "node_state",
        "send_time",
    };
    return (field >= 0 && field < 15) ? fieldNames[field] : nullptr;
}

int packet_frameDescriptor::findField(const char *fieldName) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    int base = basedesc ? basedesc->getFieldCount() : 0;
    if (fieldName[0] == 'd' && strcmp(fieldName, "dest_id") == 0)
        return base + 0;
    if (fieldName[0] == 's' && strcmp(fieldName, "source_id") == 0)
        return base + 1;
    if (fieldName[0] == 's' && strcmp(fieldName, "sender_id") == 0)
        return base + 2;
    if (fieldName[0] == 'm' && strcmp(fieldName, "msg_type") == 0)
        return base + 3;
    if (fieldName[0] == 'm' && strcmp(fieldName, "msg_id") == 0)
        return base + 4;
    if (fieldName[0] == 'c' && strcmp(fieldName, "charge_cycle") == 0)
        return base + 5;
    if (fieldName[0] == 'o' && strcmp(fieldName, "origin_slot") == 0)
        return base + 6;
    if (fieldName[0] == 'c' && strcmp(fieldName, "current_slot") == 0)
        return base + 7;
    if (fieldName[0] == 'l' && strcmp(fieldName, "lag_bias") == 0)
        return base + 8;
    if (fieldName[0] == 'd' && strcmp(fieldName, "delay_bias") == 0)
        return base + 9;
    if (fieldName[0] == 's' && strcmp(fieldName, "sender_type") == 0)
        return base + 10;
    if (fieldName[0] == 'n' && strcmp(fieldName, "next_id") == 0)
        return base + 11;
    if (fieldName[0] == 'p' && strcmp(fieldName, "pass_counter") == 0)
        return base + 12;
    if (fieldName[0] == 'n' && strcmp(fieldName, "node_state") == 0)
        return base + 13;
    if (fieldName[0] == 's' && strcmp(fieldName, "send_time") == 0)
        return base + 14;
    return basedesc ? basedesc->findField(fieldName) : -1;
}

const char *packet_frameDescriptor::getFieldTypeString(int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldTypeString(field);
        field -= basedesc->getFieldCount();
    }
    static const char *fieldTypeStrings[] = {
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "int",
        "simtime_t",
    };
    return (field >= 0 && field < 15) ? fieldTypeStrings[field] : nullptr;
}

const char **packet_frameDescriptor::getFieldPropertyNames(int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldPropertyNames(field);
        field -= basedesc->getFieldCount();
    }
    switch (field)
    {
    default:
        return nullptr;
    }
}

const char *packet_frameDescriptor::getFieldProperty(int field, const char *propertyname) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldProperty(field, propertyname);
        field -= basedesc->getFieldCount();
    }
    switch (field)
    {
    default:
        return nullptr;
    }
}

int packet_frameDescriptor::getFieldArraySize(void *object, int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldArraySize(object, field);
        field -= basedesc->getFieldCount();
    }
    packet_frame *pp = (packet_frame *)object;
    (void)pp;
    switch (field)
    {
    default:
        return 0;
    }
}

const char *packet_frameDescriptor::getFieldDynamicTypeString(void *object, int field, int i) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldDynamicTypeString(object, field, i);
        field -= basedesc->getFieldCount();
    }
    packet_frame *pp = (packet_frame *)object;
    (void)pp;
    switch (field)
    {
    default:
        return nullptr;
    }
}

std::string packet_frameDescriptor::getFieldValueAsString(void *object, int field, int i) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldValueAsString(object, field, i);
        field -= basedesc->getFieldCount();
    }
    packet_frame *pp = (packet_frame *)object;
    (void)pp;
    switch (field)
    {
    case 0:
        return long2string(pp->getDest_id());
    case 1:
        return long2string(pp->getSource_id());
    case 2:
        return long2string(pp->getSender_id());
    case 3:
        return long2string(pp->getMsg_type());
    case 4:
        return long2string(pp->getMsg_id());
    case 5:
        return long2string(pp->getCharge_cycle());
    case 6:
        return long2string(pp->getOrigin_slot());
    case 7:
        return long2string(pp->getCurrent_slot());
    case 8:
        return long2string(pp->getLag_bias());
    case 9:
        return long2string(pp->getDelay_bias());
    case 10:
        return long2string(pp->getSender_type());
    case 11:
        return long2string(pp->getNext_id());
    case 12:
        return long2string(pp->getPass_counter());
    case 13:
        return long2string(pp->getNode_state());
    case 14:
        return simtime2string(pp->getSend_time());
    default:
        return "";
    }
}

bool packet_frameDescriptor::setFieldValueAsString(void *object, int field, int i, const char *value) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->setFieldValueAsString(object, field, i, value);
        field -= basedesc->getFieldCount();
    }
    packet_frame *pp = (packet_frame *)object;
    (void)pp;
    switch (field)
    {
    case 0:
        pp->setDest_id(string2long(value));
        return true;
    case 1:
        pp->setSource_id(string2long(value));
        return true;
    case 2:
        pp->setSender_id(string2long(value));
        return true;
    case 3:
        pp->setMsg_type(string2long(value));
        return true;
    case 4:
        pp->setMsg_id(string2long(value));
        return true;
    case 5:
        pp->setCharge_cycle(string2long(value));
        return true;
    case 6:
        pp->setOrigin_slot(string2long(value));
        return true;
    case 7:
        pp->setCurrent_slot(string2long(value));
        return true;
    case 8:
        pp->setLag_bias(string2long(value));
        return true;
    case 9:
        pp->setDelay_bias(string2long(value));
        return true;
    case 10:
        pp->setSender_type(string2long(value));
        return true;
    case 11:
        pp->setNext_id(string2long(value));
        return true;
    case 12:
        pp->setPass_counter(string2long(value));
        return true;
    case 13:
        pp->setNode_state(string2long(value));
        return true;
    case 14:
        pp->setSend_time(string2simtime(value));
        return true;
    default:
        return false;
    }
}

const char *packet_frameDescriptor::getFieldStructName(int field) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldStructName(field);
        field -= basedesc->getFieldCount();
    }
    switch (field)
    {
    default:
        return nullptr;
    };
}

void *packet_frameDescriptor::getFieldStructValuePointer(void *object, int field, int i) const
{
    omnetpp::cClassDescriptor *basedesc = getBaseClassDescriptor();
    if (basedesc)
    {
        if (field < basedesc->getFieldCount())
            return basedesc->getFieldStructValuePointer(object, field, i);
        field -= basedesc->getFieldCount();
    }
    packet_frame *pp = (packet_frame *)object;
    (void)pp;
    switch (field)
    {
    default:
        return nullptr;
    }
}
