id: 400

Code snippet:
```
@Override protected void doCatch(Throwable throwable){
  exceptionHandler.handle(throwable,getContext(),getRequest(),getResponse());
}
```
Comment:
```
Handles any exception that is thrown when processing a oauth2 authorization request.
```
---
id: 401

Code snippet:
```
public void actionPerformed(ActionEvent e){
  JTextComponent target=getTextComponent(e);
  if (target != null) {
    ComponentOrientation last=target.getComponentOrientation();
    ComponentOrientation next;
    if (last == ComponentOrientation.RIGHT_TO_LEFT)     next=ComponentOrientation.LEFT_TO_RIGHT;
 else     next=ComponentOrientation.RIGHT_TO_LEFT;
    target.setComponentOrientation(next);
    target.repaint();
  }
}
```
Comment:
```
The operation to perform when this action is triggered.
```
---
id: 402

Code snippet:
```
public void clearCachedState(){
  _autoCommitCached=null;
  _readOnlyCached=null;
  if (_conn instanceof DelegatingConnection) {
    ((DelegatingConnection<?>)_conn).clearCachedState();
  }
}
```
Comment:
```
Clears the cache.
```
---
id: 403

Code snippet:
```
private void assertBlockedLongerThanTimeout(long startTime,long endTime,int TIMEOUT){
  assertTrue(endTime - startTime >= TIMEOUT);
}
```
Comment:
```
In this scenario, the fake rs will not send back an ack so we expect the add entry code (ldap client code emulation) to be blocked for the timeout value at least. if the time we have slept is lower, timeout handling code is not working...
```
---
id: 404

Code snippet:
```
public String toString(){
  return attrSchema.toString();
}
```
Comment:
```
Method that returns the string representation of the <code>amattributeschema</code>.
```
---
id: 405

Code snippet:
```
public boolean remove(Object o){
  return map.remove(o) == PRESENT;
}
```
Comment:
```
Removes the specified element from this set if it is present. more formally, removes an element <tt>e</tt> such that <tt>(o==null&nbsp;?&nbsp;e==null&nbsp;:&nbsp;o.equals(e))</tt>, if this set contains such an element. returns <tt>true</tt> if this set contained the element (or equivalently, if this set changed as a result of the call). (this set will not contain the element once the call returns.).
```
---
id: 406

Code snippet:
```
@Override public void mark(int readlimit){
}
```
Comment:
```
Marks the current position.
```
---
id: 407

Code snippet:
```
@Inject public OAuth2Request(JacksonRepresentationFactory jacksonRepresentationFactory,@Assisted Request request){
  this.jacksonRepresentationFactory=jacksonRepresentationFactory;
  this.request=request;
}
```
Comment:
```
Creates a new exception with the specified detail message.
```
---
id: 408

Code snippet:
```
public static byte[] encode(byte[] data,int off,int length){
  ByteArrayOutputStream bOut=new ByteArrayOutputStream();
  try {
    encoder.encode(data,off,length,bOut);
  }
 catch (  Exception e) {
    throw new EncoderException(\"exception encoding Hex string: \" + e.getMessage(),e);
  }
  return bOut.toByteArray();
}
```
Comment:
```
Encode the input data producing a hex encoded byte array.
```
---
id: 409

Code snippet:
```
public NO_MEMORY(String s,int minor,CompletionStatus completed){
  super(s,minor,completed);
}
```
Comment:
```
Constructs a <code>no_memory</code> exception with the specified description message, minor code, and completion status.
```
---
id: 410

Code snippet:
```
void CreateNonCIDSubrs(int Font,IndexBaseItem PrivateBase,OffsetItem Subrs){
  OutputList.addLast(new SubrMarkerItem(Subrs,PrivateBase));
  if (NewSubrsIndexNonCID != null) {
    OutputList.addLast(new RangeItem(new RandomAccessFileOrArray(rasFactory.createSource(NewSubrsIndexNonCID)),0,NewSubrsIndexNonCID.length));
  }
}
```
Comment:
```
The function marks the beginning of the subrs index and adds the subsetted subrs index to the output list.
```
---
id: 411

Code snippet:
```
public int lastIndexOf(String string){
  return lastIndexOf(string,count);
}
```
Comment:
```
Searches for the last index of the specified character. the search for the character starts at the end and moves towards the beginning.
```
---
id: 412

Code snippet:
```
public void testConstructorSignBytesPositive1(){
  byte aBytes[]={12,56,100,-2,-76,89,45,91,3,-15};
  int aSign=1;
  byte rBytes[]={12,56,100,-2,-76,89,45,91,3,-15};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=aNumber.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(\"incorrect sign\",1,aNumber.signum());
}
```
Comment:
```
Create a positive number from a sign and an array of bytes. the number fits in an array of integers. the most significant byte is positive.
```
---
id: 413

Code snippet:
```
public static void destroyMBean(ContextResourceLink resourceLink) throws Exception {
  String mname=createManagedName(resourceLink);
  ManagedBean managed=registry.findManagedBean(mname);
  if (managed == null) {
    return;
  }
  String domain=managed.getDomain();
  if (domain == null)   domain=mserver.getDefaultDomain();
  ObjectName oname=createObjectName(domain,resourceLink);
  if (mserver.isRegistered(oname))   mserver.unregisterMBean(oname);
}
```
Comment:
```
Deregister the mbean for this <code>contextresourcelink</code> object.
```
---
id: 414

Code snippet:
```
public static MemoryMappedFile mmapRO(String path) throws ErrnoException {
  FileDescriptor fd=Libcore.os.open(path,O_RDONLY,0);
  long size=Libcore.os.fstat(fd).st_size;
  long address=Libcore.os.mmap(0L,size,PROT_READ,MAP_SHARED,fd,0);
  Libcore.os.close(fd);
  return new MemoryMappedFile(address,size);
}
```
Comment:
```
Use this to mmap the whole file read-only.
```
---
id: 415

Code snippet:
```
public boolean isAutoIncrement(int columnIndex) throws SQLException {
  checkColRange(columnIndex);
  return colInfo[columnIndex].autoIncrement;
}
```
Comment:
```
Retrieves whether a value stored in the designated column is automatically numbered, and thus readonly.
```
---
id: 416

Code snippet:
```
protected void cdata(char ch[],int start,final int length) throws org.xml.sax.SAXException {
  try {
    final int old_start=start;
    if (m_elemContext.m_startTagOpen) {
      closeStartTag();
      m_elemContext.m_startTagOpen=false;
    }
    m_ispreserve=true;
    if (shouldIndent())     indent();
    boolean writeCDataBrackets=(((length >= 1) && escapingNotNeeded(ch[start])));
    if (writeCDataBrackets && !m_cdataTagOpen) {
      m_writer.write(CDATA_DELIMITER_OPEN);
      m_cdataTagOpen=true;
    }
    if (isEscapingDisabled()) {
      charactersRaw(ch,start,length);
    }
 else     writeNormalizedChars(ch,start,length,true,m_lineSepUse);
    if (writeCDataBrackets) {
      if (ch[start + length - 1] == \']\')       closeCDATA();
    }
    if (m_tracer != null)     super.fireCDATAEvent(ch,old_start,length);
  }
 catch (  IOException ioe) {
    throw new org.xml.sax.SAXException(Utils.messages.createMessage(MsgKey.ER_OIERROR,null),ioe);
  }
}
```
Comment:
```
Receive notification of the end of an element.
```
---
id: 417

Code snippet:
```
public Set keySet(){
  return map.keySet();
}
```
Comment:
```
Returns the set of keys of this map.
```
---
id: 418

Code snippet:
```
public void testCertStore07() throws InvalidAlgorithmParameterException, NoSuchAlgorithmException {
  if (!initParams()) {
    return;
  }
  for (int i=0; i < dValid.length; i++) {
    for (int j=1; j < invalidValues.length; j++) {
      try {
        CertStore.getInstance(dValid[i],dParams,invalidValues[j]);
        fail(\"NoSuchProviderException must be thrown\");
      }
 catch (      NoSuchProviderException e) {
      }
    }
  }
}
```
Comment:
```
Test for method <code>getinstance(string type, certstoreparameters params, string provider)</code> assertion: throws nosuchproviderexception when provider has invalid value.
```
---
id: 419

Code snippet:
```
private void createSourceFiles(File parent,String childContent) throws IOException {
  if (!parent.exists()) {
    parent.mkdir();
  }
  File d1=new File(parent,\"d1\");
  File f1a=new File(d1,\"f1a\");
  File f1b=new File(d1,\"f1b\");
  File d2=new File(parent,\"d2\");
  File f2a=new File(d2,\"f2a\");
  File d2b=new File(d2,\"d2b\");
  File f2b1=new File(d2b,\"f2b1\");
  d1.mkdir();
  d2.mkdir();
  d2b.mkdir();
  writeContents(f1a,childContent);
  writeContents(f1b,childContent);
  writeContents(f2a,childContent);
  writeContents(f2b1,childContent);
}
```
Comment:
```
Creates a set of file for testing.
```
---
id: 420

Code snippet:
```
public SubjectDecision evaluate(String realm,SubjectAttributesManager mgr,Subject subject,String resourceName,Map<String,Set<String>> environment) throws EntitlementException {
  Set<EntitlementSubject> eSubjects=getESubjects();
  if ((eSubjects != null) && !eSubjects.isEmpty()) {
    for (    EntitlementSubject e : eSubjects) {
      SubjectDecision decision=e.evaluate(realm,mgr,subject,resourceName,environment);
      if (!decision.isSatisfied()) {
        return decision;
      }
    }
  }
  return new SubjectDecision(true,Collections.EMPTY_MAP);
}
```
Comment:
```
Evaluates the given algorithm.
```
---
id: 421

Code snippet:
```
public Leaves(TreeSpecies species,boolean isDecayable){
  this(DEFAULT_TYPE,species,isDecayable);
}
```
Comment:
```
Constructs a leaf block of the given tree species and flag for whether this leaf block will disappear when too far from a log.
```
---
id: 422

Code snippet:
```
public AbstractMethodError(){
  super();
}
```
Comment:
```
Constructs an <code>abstractmethoderror</code> with no detail message.
```
---
id: 423

Code snippet:
```
public int hashCode(){
  int hash=mask;
  if (rangeSet != null) {
    hash&=CONTEXTUAL_MASK;
    hash^=rangeSet.hashCode();
  }
  return hash;
}
```
Comment:
```
Returns a hash code for this shaper.
```
---
id: 424

Code snippet:
```
public static NewSuffixOptions createBaseEntry(List<String> baseDNs){
  NewSuffixOptions ops=new NewSuffixOptions(baseDNs);
  ops.type=Type.CREATE_BASE_ENTRY;
  return ops;
}
```
Comment:
```
Creates a new instance.
```
---
id: 425

Code snippet:
```
private Connection checkState(){
  if (isClosed()) {
    throw new IllegalStateException();
  }
  return connection;
}
```
Comment:
```
Checks that this pooled connection has not been closed.
```
---
id: 426

Code snippet:
```
private boolean isPropertyTrue(String propertyName){
  return \"true\".equalsIgnoreCase(getProperty(propertyName));
}
```
Comment:
```
Indicates whether the property value is set and equal to \"true\" for the supplied property name.
```
---
id: 427

Code snippet:
```
public static byte[] decode(String data){
  ByteArrayOutputStream bOut=new ByteArrayOutputStream();
  try {
    encoder.decode(data,bOut);
  }
 catch (  Exception e) {
    throw new DecoderException(\"exception decoding Hex string: \" + e.getMessage(),e);
  }
  return bOut.toByteArray();
}
```
Comment:
```
Decode the base64 encoded string.
```
---
id: 428

Code snippet:
```
public static synchronized void clearHyphenationTreeCache(){
  hTreeCache=new HyphenationTreeCache();
}
```
Comment:
```
Clears all the elements in the cache.
```
---
id: 429

Code snippet:
```
private static float centerFromEnd(int[] stateCount,int end){
  return (float)(end - stateCount[2]) - stateCount[1] / 2.0f;
}
```
Comment:
```
Returns the position of the next point in the current position.
```
---
id: 430

Code snippet:
```
public java.lang.String toString(){
  return toString(true,false);
}
```
Comment:
```
Creates a string representation of this object. by default name space name is prepended to the element name.
```
---
id: 431

Code snippet:
```
public ExpressionException(String message){
  super(message);
}
```
Comment:
```
Constructs a new exception with the specified detail message.
```
---
id: 432

Code snippet:
```
protected boolean isRepaintingRoot(){
  return isRepaintingRoot;
}
```
Comment:
```
Returns true if the component being painted is the root component that was previously passed to <code>repaintroot</code>.
```
---
id: 433

Code snippet:
```
public Set searchDynamicGroups(String wildcard,int level) throws AMException, SSOException {
  return searchDynamicGroups(wildcard,null,level);
}
```
Comment:
```
Search for the given group.
```
---
id: 434

Code snippet:
```
private XingFrame(ByteBuffer header){
  this.header=header;
  header.rewind();
  setVbr();
  byte flagBuffer[]=new byte[XING_FLAG_BUFFER_SIZE];
  header.get(flagBuffer);
  if ((flagBuffer[BYTE_4] & (byte)(1)) != 0) {
    setFrameCount();
  }
  if ((flagBuffer[BYTE_4] & (byte)(1 << 1)) != 0) {
    setAudioSize();
  }
  if (header.limit() >= XING_HEADER_BUFFER_SIZE + LameFrame.LAME_HEADER_BUFFER_SIZE) {
    header.position(XING_HEADER_BUFFER_SIZE);
    lameFrame=LameFrame.parseLameFrame(header);
  }
}
```
Comment:
```
Read the xing properties from the buffer.
```
---
id: 435

Code snippet:
```
static void storeServerList(Set servers,Map namingAttrs){
  Set serverList=new HashSet();
  Set siteList=new HashSet();
  Iterator iter=servers.iterator();
  while (iter.hasNext()) {
    String serverEntry=(String)iter.next();
    int index=serverEntry.indexOf(delimiter);
    if (index != -1) {
      String server=serverEntry.substring(0,index);
      String serverId=serverEntry.substring(index + 1,serverEntry.length());
      siteList.add(serverId);
      index=serverId.indexOf(delimiter);
      if (index != -1) {
        serverId=serverId.substring(0,2);
      }
      HashSet serverSet=new HashSet();
      serverSet.add(server);
      serverList.add(server);
      namingAttrs.put(serverId,serverSet);
    }
 else {
      namingDebug.error(\"Platform Server List entry is invalid:\" + serverEntry);
    }
  }
  namingAttrs.put(Constants.PLATFORM_LIST,serverList);
  namingAttrs.put(Constants.SITE_ID_LIST,siteList);
}
```
Comment:
```
Put a list to the database.
```
---
id: 436

Code snippet:
```
public DN child(final DN dn){
  Reject.ifNull(dn);
  if (dn.isRootDN()) {
    return this;
  }
 else   if (isRootDN()) {
    return dn;
  }
 else {
    final RDN[] rdns=new RDN[dn.size()];
    int i=rdns.length;
    for (DN next=dn; next.rdn != null; next=next.parent) {
      rdns[--i]=next.rdn;
    }
    DN newDN=this;
    for (i=0; i < rdns.length; i++) {
      newDN=new DN(this.schema,newDN,rdns[i]);
    }
    return newDN;
  }
}
```
Comment:
```
Returns a dn which is subordinate to this dn and having the additional rdn components contained in the provided dn.
```
---
id: 437

Code snippet:
```
public boolean processNotificationHandlerConfig(ErrorLogAccountStatusNotificationHandlerCfg configuration,boolean applyChanges){
  boolean isAcceptable=true;
  HashSet<AccountStatusNotificationType> newNotificationTypes=new HashSet<>();
  for (  ErrorLogAccountStatusNotificationHandlerCfgDefn.AccountStatusNotificationType configNotificationType : configuration.getAccountStatusNotificationType()) {
    newNotificationTypes.add(getNotificationType(configNotificationType));
  }
  if (applyChanges && isAcceptable) {
    notificationTypes=newNotificationTypes;
  }
  return isAcceptable;
}
```
Comment:
```
Parses the provided configuration and configure the notification handler.
```
---
id: 438

Code snippet:
```
public com.sun.identity.wsfederation.jaxb.xmlsig.DSAKeyValueElement createDSAKeyValueElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.wsfederation.jaxb.xmlsig.impl.DSAKeyValueElementImpl();
}
```
Comment:
```
Create an instance of dsakeyvalueelement.
```
---
id: 439

Code snippet:
```
static public PrintWriter log(Throwable xcpt,PrintWriter out){
  out.println(\"-----------\");
  out.println(xcpt.toString());
  out.println(\"Stack Trace:\");
  out.print(getStackTrace(xcpt));
  out.println(\"-----------\");
  out.flush();
  return out;
}
```
Comment:
```
Formats an exception to a <code>printwriter</code>.
```
---
id: 440

Code snippet:
```
public JKXmlException(String message,Throwable cause){
  super(message,cause);
}
```
Comment:
```
Instantiates a new jk xml exception.
```
---
id: 441

Code snippet:
```
public DTMIterator createDTMIterator(Object xpathCompiler,int pos){
  return m_dtmManager.createDTMIterator(xpathCompiler,pos);
}
```
Comment:
```
Creates a new instance.
```
---
id: 442

Code snippet:
```
public FactoryConfigurationError(java.lang.String msg){
  super(msg);
}
```
Comment:
```
Creates a new <code>reason</code> with the specified detail message.
```
---
id: 443

Code snippet:
```
public Period withYears(int years){
  if (years == this.years) {
    return this;
  }
  return create(years,months,days);
}
```
Comment:
```
Returns a string representation of this period.
```
---
id: 444

Code snippet:
```
public void paintSliderThumbBorder(SynthContext context,Graphics g,int x,int y,int w,int h,int orientation){
}
```
Comment:
```
Paints the border of the thumb of a slider.
```
---
id: 445

Code snippet:
```
public Pumpkin(BlockFace direction){
  this();
  setFacingDirection(direction);
}
```
Comment:
```
Creates a new instance.
```
---
id: 446

Code snippet:
```
public Guid(long id){
  _dn=DN.valueOf(\"\");
  _uniqueId=id;
}
```
Comment:
```
Creates a new instance.
```
---
id: 447

Code snippet:
```
public EncryptableNameIdentifier(String name,String nameQualifier,String format,Date issueInstant,String nonce) throws FSException {
  if (name == null || nameQualifier == null || issueInstant == null || format == null || nonce == null) {
    throw new FSException(\"nullInput\",null);
  }
  _name=name;
  _nameQualifier=nameQualifier;
  _format=format;
  _nonce=nonce;
  _issueInstant=issueInstant;
}
```
Comment:
```
Creates a new instance.
```
---
id: 448

Code snippet:
```
public void startElement(String elementNamespaceURI,String elementLocalName,String elementName) throws SAXException {
  startElement(elementNamespaceURI,elementLocalName,elementName,null);
}
```
Comment:
```
Receive notification of the beginning of an element, additional namespace or attribute information can occur before or after this call, that is associated with this element.
```
---
id: 449

Code snippet:
```
private void init(String servicePrincipal,int mask){
  if (servicePrincipal == null)   throw new NullPointerException(\"service principal can\'t be null\");
  if ((mask & ALL) != mask)   throw new IllegalArgumentException(\"invalid actions mask\");
  this.mask=mask;
}
```
Comment:
```
Initialise the service.
```
---
id: 450

Code snippet:
```
protected ServerConstraintHandler(){
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 451

Code snippet:
```
@Inject public OpenIdConnectAuthorizeRequestValidator(ClientRegistrationStore clientRegistrationStore){
  this.clientRegistrationStore=clientRegistrationStore;
}
```
Comment:
```
Constructs a new openidconnectauthorizerequestvalidator instance.
```
---
id: 452

Code snippet:
```
public int doFinal(byte[] out,int outOff) throws DataLengthException, IllegalStateException, InvalidCipherTextException {
  int blockSize=cipher.getBlockSize();
  int resultLen=0;
  if (forEncryption) {
    if (bufOff == blockSize) {
      if ((outOff + 2 * blockSize) > out.length) {
        reset();
        throw new OutputLengthException(\"output buffer too short\");
      }
      resultLen=cipher.processBlock(buf,0,out,outOff);
      bufOff=0;
    }
    padding.addPadding(buf,bufOff);
    resultLen+=cipher.processBlock(buf,0,out,outOff + resultLen);
    reset();
  }
 else {
    if (bufOff == blockSize) {
      resultLen=cipher.processBlock(buf,0,buf,0);
      bufOff=0;
    }
 else {
      reset();
      throw new DataLengthException(\"last block incomplete in decryption\");
    }
    try {
      resultLen-=padding.padCount(buf);
      System.arraycopy(buf,0,out,outOff,resultLen);
    }
  finally {
      reset();
    }
  }
  return resultLen;
}
```
Comment:
```
Process the next block.
```
---
id: 453

Code snippet:
```
public static ASN1Primitive convertValueToObject(X509Extension ext) throws IllegalArgumentException {
  try {
    return ASN1Primitive.fromByteArray(ext.getValue().getOctets());
  }
 catch (  IOException e) {
    throw new IllegalArgumentException(\"can\'t convert extension: \" + e);
  }
}
```
Comment:
```
Convert a string to a string.
```
---
id: 454

Code snippet:
```
private static byte[] procIPv4Addr(String addrStr,BitSet wildCardBitSet,String expr) throws AciException {
  byte[] addrBytes=new byte[IN4ADDRSZ];
  String[] s=addrStr.split(\"\\.\",-1);
  try {
    if (s.length != IN4ADDRSZ) {
      LocalizableMessage message=WARN_ACI_SYNTAX_INVALID_IPV4_FORMAT.get(expr);
      throw new AciException(message);
    }
    for (int i=0; i < IN4ADDRSZ; i++) {
      String quad=s[i].trim();
      if (quad.equals(\"*\")) {
        wildCardBitSet.set(i);
      }
 else {
        long val=Integer.parseInt(quad);
        if (val < 0 || val > 0xff) {
          LocalizableMessage message=WARN_ACI_SYNTAX_INVALID_IPV4_VALUE.get(expr);
          throw new AciException(message);
        }
        addrBytes[i]=(byte)(val & 0xff);
      }
    }
  }
 catch (  NumberFormatException nfex) {
    LocalizableMessage message=WARN_ACI_SYNTAX_IPV4_NOT_NUMERIC.get(expr);
    throw new AciException(message);
  }
  return addrBytes;
}
```
Comment:
```
Process the provided ipv4 address string parsed from the ip bind rule address expression. it returns a byte array corresponding to the address string. the specified bit set represents wild-card characters \'*\' found in the string.
```
---
id: 455

Code snippet:
```
int numCharCountBits(int ver){
  if (1 <= ver && ver <= 9)   return numBitsCharCount[0];
 else   if (10 <= ver && ver <= 26)   return numBitsCharCount[1];
 else   if (27 <= ver && ver <= 40)   return numBitsCharCount[2];
 else   throw new IllegalArgumentException(\"Version number out of range\");
}
```
Comment:
```
Returns the number of bits in the given range.
```
---
id: 456

Code snippet:
```
void componentInputMapChanged(ComponentInputMap inputMap){
  InputMap km=getInputMap(WHEN_IN_FOCUSED_WINDOW,false);
  while (km != inputMap && km != null) {
    km=km.getParent();
  }
  if (km != null) {
    registerWithKeyboardManager(false);
  }
}
```
Comment:
```
Invoked from <code>componentinputmap</code> when its bindings change. if <code>inputmap</code> is the current <code>windowinputmap</code> (or a parent of the window <code>inputmap</code>) the <code>keyboardmanager</code> is notified of the new bindings.
```
---
id: 457

Code snippet:
```
@Override protected void shareText(final ShareParamText params) throws ShareException {
  checkContent(params);
  final WeiboMultiMessage weiboMessage=new WeiboMultiMessage();
  weiboMessage.textObject=getTextObj(params);
  allInOneShare(weiboMessage);
}
```
Comment:
```
Contont cannot be empty.
```
---
id: 458

Code snippet:
```
@SuppressWarnings(\"unchecked\") public static <T>void sort(List<T> list,Comparator<? super T> comparator){
  T[] array=list.toArray((T[])new Object[list.size()]);
  Arrays.sort(array,comparator);
  int i=0;
  ListIterator<T> it=list.listIterator();
  while (it.hasNext()) {
    it.next();
    it.set(array[i++]);
  }
}
```
Comment:
```
Sorts the given list using the given comparator. the algorithm is stable which means equal elements don\'t get reordered.
```
---
id: 459

Code snippet:
```
public SMSubConfig(String id,String name,String type,String localizedName,boolean hidden){
  this.id=id;
  this.name=name;
  this.type=type;
  this.localizedName=localizedName;
  this.hidden=hidden;
}
```
Comment:
```
Creates a new instance of the class.
```
---
id: 460

Code snippet:
```
public SizeSequence(int[] sizes){
  this();
  setSizes(sizes);
}
```
Comment:
```
Creates a new <code>sizesequence</code> object that contains the specified sizes.
```
---
id: 461

Code snippet:
```
public void testCase14(){
  byte aBytes[]={1,2,3,4,5,6,7,1,2,3,4,5,6,7};
  byte bBytes[]={10,20,30,40,50,60,70,10,20,30};
  int aSign=-1;
  int bSign=1;
  byte rBytes[]={-2,-3,-4,-5,-16,-27,-38,-42,-53,-64,-75,-16,-27,-37};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger bNumber=new BigInteger(bSign,bBytes);
  BigInteger result=aNumber.subtract(bNumber);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(-1,result.signum());
}
```
Comment:
```
Subtract two numbers of the same length and different signs. the first is negative. the second is longer.
```
---
id: 462

Code snippet:
```
public DeleteContext(CSN csn,String entryUUID){
  super(csn,entryUUID);
}
```
Comment:
```
Creates a new deletecontext with the provided information.
```
---
id: 463

Code snippet:
```
public void handleButton3Request(RequestInvocationEvent event) throws ModelControlException, AMConsoleException {
  removePageSessionAttribute(PAGE_MODIFIED);
  backTrail();
  try {
    String name=(String)getPageSessionAttribute(AMAdminConstants.SAVE_VB_NAME);
    SCConfigViewBean vb=(SCConfigViewBean)getViewBean(Class.forName(name));
    passPgSessionMap(vb);
    vb.forwardTo(getRequestContext());
  }
 catch (  ClassNotFoundException e) {
    debug.warning(\"SCSAML2SOAPBindingViewBean.handleButton3Request:\",e);
  }
}
```
Comment:
```
Handles reset request.
```
---
id: 464

Code snippet:
```
public void resetTagDefinitions(){
  mTagInfo=null;
}
```
Comment:
```
Reset the cache.
```
---
id: 465

Code snippet:
```
public void testClearBitPositiveOutside1(){
  byte aBytes[]={1,-128,56,100,-2,-76,89,45,91,3,-15,35,26};
  int aSign=1;
  int number=150;
  byte rBytes[]={1,-128,56,100,-2,-76,89,45,91,3,-15,35,26};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger result=aNumber.clearBit(number);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(\"incorrect sign\",1,result.signum());
}
```
Comment:
```
Clearbit(int n) outside a positive number.
```
---
id: 466

Code snippet:
```
public void reset(){
  gsStack.removeAllElements();
  gsStack.push(new ParserGraphicsState());
  textMatrix=null;
  textLineMatrix=null;
  resourcesStack=new Stack<>();
  isClip=false;
  currentPath=new Path();
}
```
Comment:
```
Resets the graphics state stack, matrices and resources.
```
---
id: 467

Code snippet:
```
public Object clone(){
  SipUri retval=(SipUri)super.clone();
  if (this.authority != null)   retval.authority=(Authority)this.authority.clone();
  if (this.uriParms != null)   retval.uriParms=(NameValueList)this.uriParms.clone();
  if (this.qheaders != null)   retval.qheaders=(NameValueList)this.qheaders.clone();
  if (this.telephoneSubscriber != null)   retval.telephoneSubscriber=(TelephoneNumber)this.telephoneSubscriber.clone();
  return retval;
}
```
Comment:
```
Deep clone.
```
---
id: 468

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  Node ownerElement;
  Attr attr;
  doc=(Document)load(\"staffNS\",false);
  attr=doc.createAttributeNS(\"http://www.w3.org/DOM\",\"dom:attr\");
  ownerElement=attr.getOwnerElement();
  assertNull(\"attrgetownerelement03\",ownerElement);
}
```
Comment:
```
Runs the test case.
```
---
id: 469

Code snippet:
```
private static boolean isValueAbsent(String s){
  return s == null || s.length() == 0;
}
```
Comment:
```
Returns true if the given string is a string.
```
---
id: 470

Code snippet:
```
@Override public void onResume(){
  super.onResume();
  Log.d(TAG,\"FMRadio onResume isGestureOpen = \" + isGestureOpen());
  if (isFmRadioGestureSupport() && isGestureOpen()) {
    resumePsensor();
  }
  Log.d(TAG,\"FmRadioActivity.onResume start\");
  mIsActivityForeground=true;
  if (null == mService) {
    Log.d(TAG,\"service has not bind finished\");
    mIsNeedShowNoAntennaDlg=false;
    return;
  }
  updateMenuStatus();
  updateDialogStatus();
  if (!isRecordFileExist()) {
    mButtonPlayback.setEnabled(false);
  }
  checkNoAntennaDialogInOnResume();
  Log.d(TAG,\"FmRadioActivity.onResume end\");
}
```
Comment:
```
Refresh ui, when stop search, dismiss search dialog, pop up recording dialog if fm stopped when recording in background.
```
---
id: 471

Code snippet:
```
public Encoder withoutPadding(){
  if (!doPadding)   return this;
  return new Encoder(isURL,newline,linemax,false);
}
```
Comment:
```
Returns an encoder instance that encodes equivalently to this one, but without adding any padding character at the end of the encoded byte data. <p> the encoding scheme of this encoder instance is unaffected by this invocation. the returned encoder instance should be used for non-padding encoding operation.
```
---
id: 472

Code snippet:
```
public SelectorContext(Hashtable<String,Object> env,boolean initialContext){
  this.env=env;
  this.initialContext=initialContext;
}
```
Comment:
```
Creates a new instance.
```
---
id: 473

Code snippet:
```
public JColorChooser(Color initialColor){
  this(new DefaultColorSelectionModel(initialColor));
}
```
Comment:
```
Creates a color chooser pane with the specified initial color.
```
---
id: 474

Code snippet:
```
protected boolean isIgnoredProfile(String realm){
  return true;
}
```
Comment:
```
Returns true if the given file is a file.
```
---
id: 475

Code snippet:
```
public void test_getInstanceLjava_lang_StringLjava_lang_String01() throws Exception {
  for (  String validValue : getValidValues()) {
    try {
      TrustManagerFactory.getInstance(validValue,(String)null);
      fail();
    }
 catch (    IllegalArgumentException expected) {
    }
    try {
      TrustManagerFactory.getInstance(validValue,\"\");
      fail();
    }
 catch (    IllegalArgumentException expected) {
    }
  }
}
```
Comment:
```
Test for <code>getinstance(string algorithm, string provider)</code> method assertion: throws illegalargumentexception when provider is null or empty.
```
---
id: 476

Code snippet:
```
public static KeyManager[] wrap(KeyManager[] keyManagers,SortedSet<String> aliases,String componentName){
  final KeyManager[] newKeyManagers=new KeyManager[keyManagers.length];
  for (int i=0; i < keyManagers.length; i++) {
    newKeyManagers[i]=new SelectableCertificateKeyManager((X509KeyManager)keyManagers[i],aliases,componentName);
  }
  return newKeyManagers;
}
```
Comment:
```
Wraps the provided set of key managers in selectable certificate key managers using the provided alias.
```
---
id: 477

Code snippet:
```
public void handleButton2Request(RequestInvocationEvent event){
  populateValues=true;
  repopulateMechID();
  forwardTo();
}
```
Comment:
```
Handles reset request.
```
---
id: 478

Code snippet:
```
public static String toLatinAlphabetNumberUpperCase(int number){
  return AlphabetNumbering.toAlphabetNumber(number,ALPHABET_UPPERCASE);
}
```
Comment:
```
Convert a string to a string.
```
---
id: 479

Code snippet:
```
public boolean inDaylightTime(Date date){
  return (getOffset(date.getTime()) != rawOffset);
}
```
Comment:
```
Returns true if the given date is a date.
```
---
id: 480

Code snippet:
```
public void deleteField(FieldKey genericKey){
  if (genericKey == FieldKey.TRACK) {
    track=0;
  }
 else {
    super.deleteField(genericKey);
  }
}
```
Comment:
```
Deletes a key.
```
---
id: 481

Code snippet:
```
public MalformedURLException(){
}
```
Comment:
```
Constructs a new <code>sqlexception</code> with the specified detail message.
```
---
id: 482

Code snippet:
```
private boolean isDualRole(EntityDescriptorElement entityDescriptor){
  boolean dual=false;
  if (entityDescriptor != null) {
    if ((SAML2MetaUtils.getSPSSODescriptor(entityDescriptor) != null) && (SAML2MetaUtils.getIDPSSODescriptor(entityDescriptor) != null)) {
      dual=true;
    }
  }
  return dual;
}
```
Comment:
```
Retrieves information whether entity has dual role or not.
```
---
id: 483

Code snippet:
```
public FileWriter(String fileName,boolean append) throws IOException {
  super(new FileOutputStream(fileName,append));
}
```
Comment:
```
Constructs a filewriter object given a file name with a boolean indicating whether or not to append the data written.
```
---
id: 484

Code snippet:
```
public PdfCanvas moveTextWithLeading(float x,float y){
  currentGs.setLeading(-y);
  contentStream.getOutputStream().writeFloat(x).writeSpace().writeFloat(y).writeSpace().writeBytes(TD);
  return this;
}
```
Comment:
```
Increments the number of characters in the current position.
```
---
id: 485

Code snippet:
```
public Subject(SubjectConfirmation subjectConfirmation) throws SAMLException {
  if (subjectConfirmation == null) {
    if (SAMLUtilsCommon.debug.messageEnabled()) {
      SAMLUtilsCommon.debug.message(\"Subject:  null \" + \"SubjectConfirmation specified\");
    }
    throw new SAMLRequesterException(SAMLUtilsCommon.bundle.getString(\"nullInput\"));
  }
  _subjectConfirmation=subjectConfirmation;
}
```
Comment:
```
Creates a new instance of the given class.
```
---
id: 486

Code snippet:
```
public boolean acceptFile(String filePath,String fileName){
  if (filepathMatcher == null)   return false;
  return fileName != null && filepathMatcher.reset(fileName).matches() || filePath != null && filepathMatcher.reset(filePath).matches();
}
```
Comment:
```
Returns true if the buffer\'s name or path matches the file name glob.
```
---
id: 487

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList addressList;
  Node testNode;
  NamedNodeMap attributes;
  Attr domesticAttr;
  Node s;
  doc=(Document)load(\"staff\",false);
  addressList=doc.getElementsByTagName(\"address\");
  testNode=addressList.item(0);
  attributes=testNode.getAttributes();
  domesticAttr=(Attr)attributes.getNamedItem(\"domestic\");
  s=domesticAttr.getNextSibling();
  assertNull(\"attrNextSiblingNullAssert\",s);
}
```
Comment:
```
Runs the test case.
```
---
id: 488

Code snippet:
```
@Override public long dynamicQueryCount(com.liferay.portal.kernel.dao.orm.DynamicQuery dynamicQuery,com.liferay.portal.kernel.dao.orm.Projection projection){
  return _fooLocalService.dynamicQueryCount(dynamicQuery,projection);
}
```
Comment:
```
This method is used to create a new instance.
```
---
id: 489

Code snippet:
```
@Override public void firePropertyChange(String propertyName,char oldValue,char newValue){
}
```
Comment:
```
Fires a property that can be used for the specified property.
```
---
id: 490

Code snippet:
```
public String toString(){
  return toString(true,true);
}
```
Comment:
```
Returns a string representation of this object.
```
---
id: 491

Code snippet:
```
public Result createResult() throws XACMLException {
  Object object=XACMLSDKUtils.getObjectInstance(XACMLConstants.RESULT);
  if (object == null) {
    return new ResultImpl();
  }
 else {
    return (Result)object;
  }
}
```
Comment:
```
Returns a new instance of <code>result</code>.
```
---
id: 492

Code snippet:
```
public void insertRow(final int row,final Vector rowData){
  this.dataVector.insertElementAt(rowData,row);
  justifyRows(row,row + 1);
  fireTableRowsInserted(row,row);
}
```
Comment:
```
Inserts a row at <code>row</code> in the model. the new row will contain <code>null</code> values unless <code>rowdata</code> is specified. notification of the row being added will be generated.
```
---
id: 493

Code snippet:
```
public boolean removeAll(Collection<?> c){
  Objects.requireNonNull(c);
  boolean modified=false;
  if (size() > c.size()) {
    for (Iterator<?> i=c.iterator(); i.hasNext(); )     modified|=remove(i.next());
  }
 else {
    for (Iterator<?> i=iterator(); i.hasNext(); ) {
      if (c.contains(i.next())) {
        i.remove();
        modified=true;
      }
    }
  }
  return modified;
}
```
Comment:
```
Removes from this set all of its elements that are contained in the specified collection (optional operation). if the specified collection is also a set, this operation effectively modifies this set so that its value is the <i>asymmetric set difference</i> of the two sets. <p>this implementation determines which is the smaller of this set and the specified collection, by invoking the <tt>size</tt> method on each. if this set has fewer elements, then the implementation iterates over this set, checking each element returned by the iterator in turn to see if it is contained in the specified collection. if it is so contained, it is removed from this set with the iterator\'s <tt>remove</tt> method. if the specified collection has fewer elements, then the implementation iterates over the specified collection, removing from this set each element returned by the iterator, using this set\'s <tt>remove</tt> method. <p>note that this implementation will throw an <tt>unsupportedoperationexception</tt> if the iterator returned by the <tt>iterator</tt> method does not implement the <tt>remove</tt> method.
```
---
id: 494

Code snippet:
```
private Object[] ensureCapacity(int minCapacity){
  if (tmp.length < minCapacity) {
    int newSize=minCapacity;
    newSize|=newSize >> 1;
    newSize|=newSize >> 2;
    newSize|=newSize >> 4;
    newSize|=newSize >> 8;
    newSize|=newSize >> 16;
    newSize++;
    if (newSize < 0)     newSize=minCapacity;
 else     newSize=Math.min(newSize,a.length >>> 1);
    @SuppressWarnings({\"unchecked\",\"UnnecessaryLocalVariable\"}) Object[] newArray=new Object[newSize];
    tmp=newArray;
  }
  return tmp;
}
```
Comment:
```
Ensures that the external array tmp has at least the specified number of elements, increasing its size if necessary. the size increases exponentially to ensure amortized linear time complexity.
```
---
id: 495

Code snippet:
```
public void paintSliderBorder(SynthContext context,Graphics g,int x,int y,int w,int h,int orientation){
  paintSliderBorder(context,g,x,y,w,h);
}
```
Comment:
```
Paints the border of the component.
```
---
id: 496

Code snippet:
```
public FSSAMLServiceViewBean(){
  super(\"FSSAMLService\");
  setDefaultDisplayURL(DEFAULT_DISPLAY_URL);
}
```
Comment:
```
Creates a new instance.
```
---
id: 497

Code snippet:
```
public void displayError(LocalizableMessage msg,LocalizableMessage title){
  Utilities.displayError(getFrame(),msg,title);
}
```
Comment:
```
Displays an error message dialog.
```
---
id: 498

Code snippet:
```
protected int findNext(int from){
  if (from < -1)   return -1;
  final int to=this.allHeaders.length - 1;
  boolean found=false;
  while (!found && (from < to)) {
    from++;
    found=filterHeader(from);
  }
  return found ? from : -1;
}
```
Comment:
```
Determines the index of the next header.
```
---
id: 499

Code snippet:
```
public void addAttribute(Attribute attribute,Collection<? super ByteString> duplicateValues){
  setAttribute(attribute,duplicateValues,false);
}
```
Comment:
```
Adds an attribute to the attribute.
```
---
