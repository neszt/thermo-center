// Code generated by "stringer -type ConfReg cc1101.go"; DO NOT EDIT.

package cc1101

import "strconv"

func _() {
	// An "invalid array index" compiler error signifies that the constant values have changed.
	// Re-run the stringer command to generate them again.
	var x [1]struct{}
	_ = x[IOCFG2-0]
	_ = x[IOCFG1-1]
	_ = x[IOCFG0-2]
	_ = x[FIFOTHR-3]
	_ = x[SYNC1-4]
	_ = x[SYNC0-5]
	_ = x[PKTLEN-6]
	_ = x[PKTCTRL1-7]
	_ = x[PKTCTRL0-8]
	_ = x[ADDR-9]
	_ = x[CHANNR-10]
	_ = x[FSCTRL1-11]
	_ = x[FSCTRL0-12]
	_ = x[FREQ2-13]
	_ = x[FREQ1-14]
	_ = x[FREQ0-15]
	_ = x[MDMCFG4-16]
	_ = x[MDMCFG3-17]
	_ = x[MDMCFG2-18]
	_ = x[MDMCFG1-19]
	_ = x[MDMCFG0-20]
	_ = x[DEVIATN-21]
	_ = x[MCSM2-22]
	_ = x[MCSM1-23]
	_ = x[MCSM0-24]
	_ = x[FOCCFG-25]
	_ = x[BSCFG-26]
	_ = x[AGCCTRL2-27]
	_ = x[AGCCTRL1-28]
	_ = x[AGCCTRL0-29]
	_ = x[WOREVT1-30]
	_ = x[WOREVT0-31]
	_ = x[WORCTRL-32]
	_ = x[FREND1-33]
	_ = x[FREND0-34]
	_ = x[FSCAL3-35]
	_ = x[FSCAL2-36]
	_ = x[FSCAL1-37]
	_ = x[FSCAL0-38]
	_ = x[RCCTRL1-39]
	_ = x[RCCTRL0-40]
	_ = x[FSTEST-41]
	_ = x[PTEST-42]
	_ = x[AGCTEST-43]
	_ = x[TEST2-44]
	_ = x[TEST1-45]
	_ = x[TEST0-46]
	_ = x[PATABLE-62]
}

const (
	_ConfReg_name_0 = "IOCFG2IOCFG1IOCFG0FIFOTHRSYNC1SYNC0PKTLENPKTCTRL1PKTCTRL0ADDRCHANNRFSCTRL1FSCTRL0FREQ2FREQ1FREQ0MDMCFG4MDMCFG3MDMCFG2MDMCFG1MDMCFG0DEVIATNMCSM2MCSM1MCSM0FOCCFGBSCFGAGCCTRL2AGCCTRL1AGCCTRL0WOREVT1WOREVT0WORCTRLFREND1FREND0FSCAL3FSCAL2FSCAL1FSCAL0RCCTRL1RCCTRL0FSTESTPTESTAGCTESTTEST2TEST1TEST0"
	_ConfReg_name_1 = "PATABLE"
)

var (
	_ConfReg_index_0 = [...]uint16{0, 6, 12, 18, 25, 30, 35, 41, 49, 57, 61, 67, 74, 81, 86, 91, 96, 103, 110, 117, 124, 131, 138, 143, 148, 153, 159, 164, 172, 180, 188, 195, 202, 209, 215, 221, 227, 233, 239, 245, 252, 259, 265, 270, 277, 282, 287, 292}
)

func (i ConfReg) String() string {
	switch {
	case i <= 46:
		return _ConfReg_name_0[_ConfReg_index_0[i]:_ConfReg_index_0[i+1]]
	case i == 62:
		return _ConfReg_name_1
	default:
		return "ConfReg(" + strconv.FormatInt(int64(i), 10) + ")"
	}
}
